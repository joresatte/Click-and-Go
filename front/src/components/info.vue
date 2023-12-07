<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<template>
  <div class="info">
    <h4 class="green">{{ msg }}</h4>
  </div>
</template>

<style scoped>

@media (min-width: 1024px) {
  .info h4 {
    text-align: left;
  }
}
</style>
