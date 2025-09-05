import { Controller, Delete, Get, Post, Put } from '@nestjs/common';
import { TasksService } from './tasks.service';

@Controller('tasks')
export class TasksController {
  constructor(private readonly tasksService: TasksService) {}

  @Get()
  findAll() {
    return this.tasksService.findAll();
  }

  // TODO: Implement the create endpoint
  @Post()
  create() {
    return {};
  }

  // TODO: Implement the update endpoint
  @Put()
  update() {
    return {};
  }

  // TODO: Implement the remove endpoint
  @Delete()
  remove() {
    return {};
  }
}
