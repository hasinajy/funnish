import { IsEnum, IsString } from 'class-validator';
import { TaskPriority } from '../enums/task-priority.enum';

export class TaskDto {
  @IsString()
  description: string;

  @IsEnum(TaskPriority)
  priority: TaskPriority;
}
