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

  @Post()
  create(@Body() createTaskDto: CreateTaskDto) {
    return this.tasksService.create(createTaskDto);
  }

  @Put(':id')
  update(@Param('id') taskId: string, @Body() createTaskDto: CreateTaskDto) {
    return this.tasksService.update(taskId, createTaskDto);
  }

  @Delete(':id')
  remove(@Param('id') taskId: string) {
    return this.tasksService.remove(taskId);
  }
}
