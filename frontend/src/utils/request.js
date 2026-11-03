import axios from "axios";

// 创建 axios 实例
const service = axios.create({
  // 🎯 设置基础 URL：优先读取环境变量，如果没有则默认走 /api (配合 vite 代理)
  baseURL: import.meta.env.VITE_API_BASE_URL || "/api",
  timeout: 10000, // 请求超时时间
});

// 🎯 请求拦截器
service.interceptors.request.use(
  (config) => {
    // 如果有 token，可以在这里统一挂载
    // const token = localStorage.getItem('token')
    // if (token) {
    //   config.headers['Authorization'] = `Bearer ${token}`
    // }
    return config;
  },
  (error) => {
    console.error("请求发送失败:", error);
    return Promise.reject(error);
  },
);

// 🎯 响应拦截器
service.interceptors.response.use(
  (response) => {
    // 直接返回数据体，省去组件里每次都写 res.data
    return response.data;
  },
  (error) => {
    // 全局统一错误处理
    console.error("接口响应报错:", error);
    // 如果是 404 或者 500，可以在这里统一弹窗提示
    if (error.response) {
      if (error.response.status === 404) {
        console.warn("请求的接口不存在");
      } else if (error.response.status === 500) {
        console.warn("服务器内部错误");
      }
    }
    return Promise.reject(error);
  },
);

export default service;
