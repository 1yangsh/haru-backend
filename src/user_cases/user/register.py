from end_points.user import RegisterUserRequest, RegisterUserResponse


class UserRegisterHandler:
    def handle(self, req: RegisterUserRequest) -> RegisterUserResponse:
        return RegisterUserResponse()
