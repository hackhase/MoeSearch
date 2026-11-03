import request from "../utils/request";

// 导出搜索接口
export const searchResources = (params) => {
  // 注意：这里不需要写 /api 前缀了，request.js 的 baseURL 已经处理了
  return request.get("/search/", { params });
};
