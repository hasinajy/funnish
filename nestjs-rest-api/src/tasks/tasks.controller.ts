import {
  Body,
  Controller,
  Delete,
  Get,
  Param,
  Post,
  Put
} from '@nestjs/common';
import { TasksService } from './tasks.service';
import { CreateTaskDto } from './dtos/create-task.dto';

@Controller('tasks')
export class TasksController {
  constructor(private readonly tasksService: TasksService) {}

  @Get()
  findAll() {
    return this.tasksService.findAll();
  }

  // TODO: Implement the create endpoint
  @Post()
  create(@Body() createTaskDto: CreateTaskDto) {
    return this.tasksService.create(createTaskDto);
  }

  // TODO: Implement the update endpoint
  @Put(':id')
  update(@Param('id') taskId: string, @Body() createTaskDto: CreateTaskDto) {
    return this.tasksService.update(taskId, createTaskDto);
  }

  // TODO: Implement the remove endpoint
  @Delete()
  remove() {
    return {};
  }
}
