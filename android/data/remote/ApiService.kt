package com.monitor.data.remote

import retrofit2.http.*

interface ApiService {
    @POST("metrics")
    suspend fun sendMetrics(@Header("x-api-key") key: String, @Body data: Map<String, Float>)
}