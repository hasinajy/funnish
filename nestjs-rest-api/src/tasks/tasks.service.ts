import { Injectable, NotFoundException } from '@nestjs/common';
import { Task } from 'generated/prisma';
import { PrismaService } from 'src/prisma/prisma.service';
import { TaskDto } from './dtos/task.dto';
import { PrismaClientKnownRequestError } from 'generated/prisma/runtime/library';

@Injectable()
export class TasksService {
  constructor(private readonly prisma: PrismaService) {}

  async findAll(): Promise<Task[]> {
    return this.prisma.task.findMany();
  }

  async create(taskDto: TaskDto): Promise<Task> {
    return this.prisma.task.create({ data: taskDto });
  }

  async update(taskId: string, taskDto: TaskDto): Promise<Task> {
    return this.prisma.task.update({
      where: {
        id: parseInt(taskId)
      },
      data: taskDto
    });
  }

  async remove(taskId: string): Promise<Task> {
    try {
      return await this.prisma.task.delete({
        where: {
          id: parseInt(taskId)
        }
      });
    } catch (error) {
      if (
        error instanceof PrismaClientKnownRequestError &&
        error.code === 'P2025'
      ) {
        throw new NotFoundException(`Task with ID "${taskId}" not found.`);
      }

      throw error;
    }
  }
}
