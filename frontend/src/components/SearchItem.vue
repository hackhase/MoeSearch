<template>
  <div class="result-card">
    <h3 class="title">
      <a
        :href="item.download_url"
        target="_blank"
        rel="noreferrer"
        referrerpolicy="no-referrer"
      >
        {{ item.title }}
      </a>
    </h3>
    <p class="desc" v-if="item.desc">{{ item.desc }}</p>
    <div class="meta">
      <span class="tag">{{ item.category }}</span>
      <span class="source">来源: {{ item.source_site || "未知" }}</span>
    </div>
  </div>
</template>

<script setup>
defineProps({
  item: { type: Object, required: true },
});
</script>

<style scoped>
.result-card {
  background: #ffffff;
  padding: 24px;
  border-radius: 12px;
  border: 1px solid #f1f5f9;
  margin-bottom: 16px;
  transition: all 0.2s ease;
  text-align: left; /* 核心：全部左对齐！ */
}
.result-card:hover {
  border-color: #cbd5e1;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
}
.title {
  margin: 0 0 10px 0;
  font-size: 18px;
  font-weight: 600;
  line-height: 1.4;
}
.title a {
  color: #1e40af; /* 类似 Google 搜索结果的蓝色 */
  text-decoration: none;
}
.title a:hover {
  text-decoration: underline;
}
.desc {
  color: #475569;
  font-size: 14px;
  line-height: 1.6;
  margin: 0 0 16px 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.meta {
  display: flex;
  align-items: center;
  gap: 16px;
  font-size: 13px;
}
.tag {
  background: #f1f5f9;
  color: #475569;
  padding: 4px 10px;
  border-radius: 999px; /* 胶囊形 */
  font-weight: 500;
}
.source {
  color: #94a3b8;
}
</style>
