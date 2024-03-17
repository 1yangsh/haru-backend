from dataclasses import dataclass


@dataclass
class UserRequest:
    email: str
    nickName: str
    imgUrl: str
    userRole: str


@dataclass
class DogRequest:
    name: str
    weight: float
    gender: str
    birthday: str
    imgUrl: str


@dataclass
class RegisterUserRequest:
    userRequest: UserRequest
    dogRequest: DogRequest
    homeName: str
