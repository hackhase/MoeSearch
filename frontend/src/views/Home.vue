<template>
  <div class="page-wrapper">
    <div class="container">
      <!-- 头部区域 -->
      <div class="header" :class="{ 'is-searched': searched }">
        <h1 class="logo">MoeSearch<span class="dot">.</span></h1>
        <p class="subtitle" v-if="!searched">
          一个极简、极速的开源资源搜索引擎
        </p>
      </div>

      <!-- 搜索框 -->
      <SearchBar v-model="keyword" @search="handleSearch(1)" />

      <!-- 结果列表 -->
      <div class="results" v-if="results.length > 0">
        <SearchItem v-for="item in results" :key="item.id" :item="item" />
        <Pagination
          :current-page="page"
          :total-page="totalPage"
          @change-page="handleSearch"
        />
      </div>

      <div v-else-if="searched" class="empty">
        <p>没有找到关于 "{{ lastKeyword }}" 的资源 (╥﹏╥)</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import SearchBar from "../components/SearchBar.vue";
import SearchItem from "../components/SearchItem.vue";
import Pagination from "../components/Pagination.vue";
import { searchResources } from "../api/search";

const keyword = ref("");
const lastKeyword = ref("");
const results = ref([]);
const searched = ref(false);
const page = ref(1);
const total = ref(0);

// 计算总页数，每页 20 条
const totalPage = computed(() => Math.ceil(total.value / 20) || 1);

const handleSearch = async (targetPage) => {
  if (!keyword.value.trim() || targetPage < 1) return;

  lastKeyword.value = keyword.value;
  page.value = targetPage;

  try {
    const res = await searchResources({
      keyword: keyword.value,
      page: targetPage,
    });
    // 🎯 修改这里：因为拦截器已经处理了 data，所以直接使用 res
    results.value = res.results;
    total.value = res.count;
    searched.value = true;
    window.scrollTo({ top: 0, behavior: "smooth" });
  } catch (error) {
    console.error("搜索请求失败", error);
    alert("请求失败，请检查后端服务是否开启");
  }
};
</script>

<style scoped>
.page-wrapper {
  min-height: 100vh;
  background-color: #f8fafc; /* 极浅的灰蓝色背景 */
  padding-top: 80px;
}
.container {
  max-width: 760px; /* 收窄一点，最适合阅读的宽度 */
  margin: 0 auto;
  padding: 0 20px 60px;
}

/* 初始状态的动画：居中且大气 */
.header {
  text-align: center;
  margin-bottom: 40px;
  transition: all 0.4s ease;
}
.header.is-searched {
  margin-bottom: 30px;
}

.logo {
  font-size: 40px;
  font-weight: 800;
  color: #0f172a;
  letter-spacing: -1px;
  margin: 0 0 10px 0;
}
.dot {
  color: #3b82f6; /* 结尾加个蓝色小点，极客最爱 */
}
.subtitle {
  color: #64748b;
  font-size: 16px;
  margin: 0;
}
.empty {
  text-align: center;
  color: #94a3b8;
  font-size: 16px;
  margin-top: 60px;
}
</style>
