-- CreateTable
CREATE TABLE "public"."Task" (
    "id" SERIAL NOT NULL,
    "description" TEXT NOT NULL,

    CONSTRAINT "Task_pkey" PRIMARY KEY ("id")
);
