import { Injectable } from '@nestjs/common';
import { Task } from 'generated/prisma';
import { PrismaService } from 'src/prisma/prisma.service';
import { CreateTaskDto } from './dtos/create-task.dto';

@Injectable()
export class TasksService {
  constructor(private readonly prisma: PrismaService) {}

  async findAll(): Promise<Task[]> {
    return this.prisma.task.findMany();
  }

  async create(createTaskDto: CreateTaskDto): Promise<Task> {
    return this.prisma.task.create({ data: createTaskDto });
  }

  async update(taskId: string, createTaskDto: CreateTaskDto): Promise<Task> {
    return this.prisma.task.update({
      where: {
        id: parseInt(taskId)
      },
      data: createTaskDto
    });
  }

  async remove(taskId: string): Promise<Task> {
    return this.prisma.task.delete({
      where: {
        id: parseInt(taskId)
      }
    });
  }
}
