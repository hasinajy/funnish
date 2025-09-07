export class AuthResponseDto {
  access_token: string;
  user: {
    id: number;
    username: string;
  };
}

export class RegisterResponseDto {
  id: number;
  username: string;
}
