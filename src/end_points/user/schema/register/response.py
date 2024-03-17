from dataclasses import dataclass


@dataclass
class UserResponse:
    userId: str
    email: str
    imgUrl: str
    nickName: str
    userRole: str
    allowNotification: str
    dogId: int
    homeId: str


@dataclass
class HomeResponse:
    homeId: str
    homeName: str


@dataclass
class DogResponse:
    dogId: int
    name: str
    weight: float
    gender: str
    birthday: str
    imgUrl: str


@dataclass
class Token:
    tokenKey: str
    accessToken: str
    refreshToken: str


@dataclass
class Data:
    userResponse: UserResponse
    homeResponse: HomeResponse
    dogResponse: DogResponse
    token: Token


@dataclass
class RegisterUserResponse:
    status: str
    message: str
    data: Data
