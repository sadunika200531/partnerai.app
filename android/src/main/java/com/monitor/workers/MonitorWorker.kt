package com.monitor.workers

import android.content.Context
import androidx.work.CoroutineWorker
import androidx.work.WorkerParameters

class MonitorWorker(ctx: Context, params: WorkerParameters) : CoroutineWorker(ctx, params) {
    override suspend fun doWork(): Result {
        // Logic to fetch metrics and trigger notification
        return Result.success()
    }
}