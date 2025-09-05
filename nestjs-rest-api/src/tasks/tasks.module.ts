import { Module } from '@nestjs/common';
import { PrismaModule } from 'src/prisma/prisma.module';
import { TasksService } from './tasks.service';

@Module({
  imports: [PrismaModule],
  providers: [TasksService]
})
export class TasksModule {}
