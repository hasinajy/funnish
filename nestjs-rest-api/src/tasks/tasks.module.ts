import { Module } from '@nestjs/common';
import { PrismaModule } from 'src/prisma/prisma.module';
import { TasksService } from './tasks.service';
import { TasksController } from './tasks.controller';

@Module({
  imports: [PrismaModule],
  providers: [TasksService],
  controllers: [TasksController]
})
export class TasksModule {}
