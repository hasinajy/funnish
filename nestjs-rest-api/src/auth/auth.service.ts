import { JwtPayload } from './../../node_modules/@types/jsonwebtoken/index.d';
import { Injectable, UnauthorizedException } from '@nestjs/common';
import { UsersService } from '../users/users.service';
import { JwtService } from '@nestjs/jwt';
import bcrypt from 'node_modules/bcryptjs';
import { User } from 'generated/prisma';

@Injectable()
export class AuthService {
  constructor(
    private readonly usersService: UsersService,
    private readonly jwtService: JwtService
  ) {}

  async validateUser(username: string, password: string): Promise<any> {
    const user = await this.usersService.findByUsername(username);
    if (user && (await bcrypt.compare(password, user.passwordHash))) {
      const { passwordHash, ...result } = user;
      return result;
    }
    return null;
  }

  async login(username: string, password: string) {
    const user: User = await this.validateUser(username, password);
    if (!user) {
      throw new UnauthorizedException('Invalid credentials.');
    }

    const payload: JwtPayload = {
      username: user.username,
      sub: user.id.toString()
    };
    return {
      access_token: this.jwtService.sign(payload),
      user: {
        id: user.id,
        username: user.username
      }
    };
  }

  async register(username: string, password: string) {
    const saltRounds = 10;
    const passwordHash = await bcrypt.hash(password, saltRounds);

    const user = await this.usersService.create({
      username,
      passwordHash
    });

    const { passwordHash: _, ...userWithoutPassword } = user;
    return userWithoutPassword;
  }
}
