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
import { TaskDto } from './dtos/task.dto';

@Controller('tasks')
export class TasksController {
  constructor(private readonly tasksService: TasksService) {}

  @Get()
  findAll() {
    return this.tasksService.findAll();
  }

  @Post()
  create(@Body() taskDto: TaskDto) {
    return this.tasksService.create(taskDto);
  }

  @Put(':id')
  update(@Param('id') taskId: string, @Body() taskDto: TaskDto) {
    return this.tasksService.update(taskId, taskDto);
  }

  @Delete(':id')
  remove(@Param('id') taskId: string) {
    return this.tasksService.remove(taskId);
  }
}
