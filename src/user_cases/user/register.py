from database.sqlalchemy.database import DatabaseSession
from database.sqlalchemy.orm import Dog, Home, User
from end_points.user import RegisterUserRequest, RegisterUserResponse
from end_points.user.schema.register.response import (Data, DogResponse,
                                                      HomeResponse, Token,
                                                      UserResponse)


class UserRegisterHandler:
    def __init__(self, req: RegisterUserRequest):
        self.req = req

    def handle(self) -> RegisterUserResponse:
        db_session = DatabaseSession()
        with db_session.create_session() as session:
            new_dog = Dog(
                name=self.req.dogRequest.name,
                weight=self.req.dogRequest.weight,
                gender=self.req.dogRequest.gender,
                birthday=self.req.dogRequest.birthday,
                img_url=self.req.dogRequest.imgUrl,
            )
            new_home = Home(home_name=self.req.homeName, dog=new_dog)
            new_user = User(
                email=self.req.userRequest.email,
                nickname=self.req.userRequest.nickName,
                img_url=self.req.userRequest.imgUrl,
                user_role=self.req.userRequest.userRole,
                dog=new_dog,
                home=new_home,
            )
            session.add_all([new_dog, new_home, new_user])
            session.flush()
            return self.convert_user_to_response(new_user, new_dog, new_home)

    def convert_user_to_response(
        self, new_user: User, new_dog: Dog, new_home: Home
    ) -> RegisterUserResponse:
        user_response = UserResponse(
            userId=str(new_user.user_id),
            email=new_user.email,
            imgUrl=new_user.img_url,
            nickName=new_user.nickname,
            userRole=new_user.user_role,
            allowNotification=str(new_user.allow_notification),
            dogId=new_dog.dog_id,
            homeId=new_home.home_id,
        )

        home_response = HomeResponse(
            homeId=new_home.home_id, homeName=new_home.home_name
        )

        dog_response = DogResponse(
            dogId=new_dog.dog_id,
            name=new_dog.name,
            weight=new_dog.weight,
            gender=new_dog.gender,
            birthday=str(new_dog.birthday),
            imgUrl=new_dog.img_url,
        )

        token = Token(
            tokenKey="",
            accessToken="",
            refreshToken="",
        )

        data = Data(
            userResponse=user_response,
            homeResponse=home_response,
            dogResponse=dog_response,
            token=token,
        )

        return RegisterUserResponse(
            status="CREATED", message="User registered successfully", data=data
        )
