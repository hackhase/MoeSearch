<template>
  <div class="search-wrapper">
    <svg
      class="search-icon"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <circle cx="11" cy="11" r="8"></circle>
      <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
    </svg>
    <input
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      @keyup.enter="$emit('search')"
      placeholder="输入关键词，如：魔法、考研、PPT..."
      autofocus
    />
    <button @click="$emit('search')">搜索</button>
  </div>
</template>

<script setup>
defineProps(["modelValue"]);
defineEmits(["update:modelValue", "search"]);
</script>

<style scoped>
.search-wrapper {
  display: flex;
  align-items: center;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 4px 8px 4px 16px;
  box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.05);
  transition: all 0.2s ease;
  margin-bottom: 40px;
}
.search-wrapper:focus-within {
  border-color: #3b82f6;
  box-shadow: 0 4px 25px -2px rgba(59, 130, 246, 0.15);
}
.search-icon {
  width: 20px;
  height: 20px;
  color: #94a3b8;
  margin-right: 12px;
}
input {
  flex: 1;
  padding: 14px 0;
  font-size: 16px;
  border: none;
  outline: none;
  background: transparent;
  color: #1e293b;
}
input::placeholder {
  color: #94a3b8;
}
button {
  padding: 12px 28px;
  font-size: 15px;
  font-weight: 500;
  background: #1e293b; /* 高级深灰色，或者用 #3b82f6 蓝色 */
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s ease;
}
button:hover {
  background: #0f172a;
}
</style>
