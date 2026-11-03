<template>
  <div class="pagination">
    <button
      @click="$emit('change-page', currentPage - 1)"
      :disabled="currentPage <= 1"
    >
      上一页
    </button>
    <span>第 {{ currentPage }} 页 / 共 {{ totalPage }} 页</span>
    <button
      @click="$emit('change-page', currentPage + 1)"
      :disabled="currentPage >= totalPage"
    >
      下一页
    </button>
  </div>
</template>

<script setup>
defineProps({
  currentPage: { type: Number, default: 1 },
  totalPage: { type: Number, default: 1 },
});
defineEmits(["change-page"]);
</script>

<style scoped>
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  margin-top: 40px;
}
button {
  padding: 10px 20px;
  border: 1px solid #ddd;
  background: #fff;
  border-radius: 8px;
  cursor: pointer;
}
button:disabled {
  background: #f5f5f5;
  color: #ccc;
  cursor: not-allowed;
}
span {
  color: #666;
  font-size: 14px;
}
</style>
