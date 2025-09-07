/*
  Warnings:

  - The `priority` column on the `Task` table would be dropped and recreated. This will lead to data loss if there is data in the column.

*/
-- CreateEnum
CREATE TYPE "public"."TaskPriority" AS ENUM ('LOW', 'MEDIUM', 'HIGH');

-- AlterTable
ALTER TABLE "public"."Task" DROP COLUMN "priority",
ADD COLUMN     "priority" "public"."TaskPriority" NOT NULL DEFAULT 'LOW';
