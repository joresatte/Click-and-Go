<template>
  <div class=" image"><img class=" mx-auto border-round" src="../assets/img/eroski.png" alt="image eroski" /></div>
</template>
<script setup>
import {ref} from 'vue'
let image= ref('')
</script>
<style scoped>
.image{
display: flex;
justify-content: center;
align-items: end;
position: relative;
margin-top: 0;
}
@media (min-width: 1024px) {
  .image {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>