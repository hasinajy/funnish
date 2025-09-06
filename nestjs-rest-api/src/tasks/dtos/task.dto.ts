import { IsInt, IsString } from 'class-validator';

export class TaskDto {
  @IsString()
  description: string;

  @IsInt()
  priority: number;
}
