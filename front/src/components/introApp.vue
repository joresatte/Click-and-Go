<!-- # @author: Jores Atte Mottoh
# @date: 14/12/2023
# @description: Component intro with methods, attributes and template
# @project: Click and Go
# @modified by:
# @modified date: -->

<template>
  <div v-if="showIntro">
    <div class="container">
      <p class="c">E</p>
      <p class="o">R</p>
      <p class="d">O</p>
      <p class="i">S</p>
      <p class="n">K</p>
      <p class="g">i</p>
    </div>
  </div>
  <span class="eroski" :style="styleObject" v-show="showContigo">{{ eroski }}</span>
</template>
<script setup>
import { ref, onMounted, reactive } from 'vue'
import { usePiniaStore } from '@/stores/store'
const piniaStore = usePiniaStore()
const showIntro = ref(true)
const eroski = ref('Contigo')
const showContigo = ref(false)
const styleObject = reactive({
  color: 'white',
  fontSize: '1em',
  backgroundColor: '',
  fontFamily: 'cursive'
})
onMounted(() => {
  setTimeout(() => {
    showIntro.value = false
    piniaStore.router.push({
      path: '/loginPage',
      name: 'loginPage'
    })
  }, 3500)
  setTimeout(() => {
    showContigo.value = true
    styleObject.color = '#021691'
    styleObject.fontSize = '2em'
    styleObject.fontFamily = 'cursive'
  }, 3000)
})
</script>
<style scoped>
*,
::before,
::after {
  /*   border: 1px solid red; */
  box-sizing: border-box;
}

* {
  margin: 0;
  padding: 0;
  font: inherit;
  transition: transform 3s ease;
}

body {
  background-image: linear-gradient(#1900ff, #f236dc, #ffeb3b);
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}
/* .container {
  width: 99%;
  height: 99%;
  background-color: transparent;
  position: relative;
  animation: bgChange 5s linear, bgScale 6s linear;
  } */

.container::before {
  content: '';
  width: 180%;
  height: 180%;
  position: absolute;
  animation: bgRotate 2s linear infinite;
  z-index: -1;
}

p {
  color: rgb(250, 7, 7);
  font-size: 30vw;
  font-family: Rubik, sans-serif;
  font-weight: 600;
  -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color: rgb(100, 100, 100);
  text-shadow:
    0px 0px 5px rgba(0, 0, 0, 0.6),
    0px 2px 15px rgba(10, 10, 10, 0.5),
    0px 5px 25px rgba(20, 20, 20, 0.4);
  margin-left: -1.9vw;
  margin-right: -1.9vw;
  position: relative;
  animation:
    rise 5s linear,
    textShadow 3s linear alternate infinite 5s;
  cursor: pointer;
}
p:hover {
  color: rgb(0, 0, 0);
  -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color: rgb(200, 200, 200);
  z-index: 11;
}
p:active {
  transform: scale(0.9);
  transition: transform 3s;
  z-index: 0;
}

.c {
  top: -2.25vh;
  z-index: 3;
}
.o {
  top: -1vh;
  z-index: 9;
}
.d {
  top: 0.5vh;
  z-index: 4;
}
.i {
  top: -0.5vh;
  z-index: 8;
}
.n {
  top: 0.25vh;
  z-index: 7;
}
.g {
  top: -1.25vh;
  z-index: 5;
}

@media (max-width: 420px) {
  ::before,
  ::after {
    box-sizing: border-box;
  }

  * {
    margin: 0;
    padding: 0;
    font: inherit;
    transition: transform 3s ease;
  }

  body {
    background-image: linear-gradient(#1900ff, #f236dc, #ffeb3b);
    width: 100vw;
    height: 100vh;
    overflow: hidden;
  }

  body,
  .container {
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    margin-top: 50%;
  }

  .container::before {
    content: '';
    width: 180%;
    height: 180%;
    position: absolute;
    animation: bgRotate 2s linear infinite;
    z-index: -1;
  }

  p {
    color: rgb(250, 7, 7);
    font-size: 30vw;
    font-family: Rubik, sans-serif;
    font-weight: 600;
    -webkit-text-stroke-width: 1px;
    -webkit-text-stroke-color: rgb(100, 100, 100);
    text-shadow:
      0px 0px 5px rgba(0, 0, 0, 0.6),
      0px 2px 15px rgba(10, 10, 10, 0.5),
      0px 5px 25px rgba(20, 20, 20, 0.4);
    margin-left: -1.9vw;
    margin-right: -1.9vw;
    position: relative;
    animation:
      rise 5s linear,
      textShadow 3s linear alternate infinite 5s;
    cursor: pointer;
  }
  p:hover {
    color: rgb(0, 0, 0);
    -webkit-text-stroke-width: 1px;
    -webkit-text-stroke-color: rgb(200, 200, 200);
    z-index: 11;
  }
  p:active {
    transform: scale(0.9);
    transition: transform 3s;
    z-index: 0;
  }

  .c {
    top: -2.25vh;
    z-index: 3;
  }
  .o {
    top: -1vh;
    z-index: 9;
  }
  .d {
    top: 0.5vh;
    z-index: 4;
  }
  .i {
    top: -0.5vh;
    z-index: 8;
  }
  .n {
    top: 0.25vh;
    z-index: 7;
  }
  .g {
    top: -1.25vh;
    z-index: 5;
  }
}

@keyframes bgChange {
  0% {
    background-color: rgb(235, 235, 235);
  }
  30% {
    background-color: rgb(235, 235, 235);
  }
  70% {
    background-color: rgb(100, 100, 100);
  }
  100% {
    background-color: rgb(10, 10, 10);
  }
}

@keyframes bgScale {
  0% {
    width: 120%;
    height: 120%;
  }
  100% {
    width: 99%;
    height: 99%;
  }
}

/* text animation */
@keyframes rise {
  0% {
    color: rgb(235, 235, 235);
    -webkit-text-stroke-width: 1px;
    -webkit-text-stroke-color: rgb(100, 100, 100);
    text-shadow:
      0px 0px 1px rgba(255, 255, 255, 0),
      0px 0px 5px rgba(0, 0, 0, 0),
      0px 2px 15px rgba(10, 10, 10, 0),
      0px 5px 25px rgba(20, 20, 20, 0);
    transform: scale(0.5);
    opacity: 0;
  }
  30% {
    color: rgb(235, 235, 235);
    text-shadow:
      0px 0px 1px rgba(255, 255, 255, 0.1),
      0px 0px 5px rgba(0, 0, 0, 0.2),
      0px 2px 15px rgba(10, 10, 10, 0.3),
      0px 5px 25px rgba(20, 20, 20, 0);
  }
  70% {
    color: rgb(100, 100, 100);
    text-shadow:
      0px 0px 2px rgba(255, 255, 255, 0.3),
      0px 0px 5px rgba(0, 0, 0, 0.6),
      0px 2px 15px rgba(10, 10, 10, 0.5),
      0px 5px 25px rgba(20, 20, 20, 0.4);
  }
  100% {
    color: rgb(238, 11, 11);
    -webkit-text-stroke-width: 1px;
    -webkit-text-stroke-color: rgb(100, 100, 100);
    text-shadow:
      0px 0px 2px rgba(255, 255, 255, 0.4),
      0px 0px 1px rgba(25, 0, 255, 0.623),
      0px 2px 4px rgba(48, 255, 252, 0.4),
      0px 5px 6px rgba(32, 8, 247, 0.658);
    opacity: 1;
  }
}

@keyframes textShadow {
  0% {
    text-shadow:
      0px 0px 2px rgba(255, 255, 255, 0.5),
      0px 0px 1px rgba(25, 0, 255, 0.3),
      0px 2px 5px rgba(48, 255, 252, 0.4),
      0px 5px 7px rgba(48, 255, 252, 0.2);
  }
  25% {
    text-shadow:
      0px 0px 2px rgba(255, 255, 255, 0.4),
      -1px -1px 2px rgba(25, 0, 255, 0.4),
      -2px -2px 6px rgba(242, 54, 220, 0.3),
      -4px -5px 8px rgba(48, 255, 252, 0.2);
  }
  50% {
    text-shadow:
      0px 0px 1px rgba(255, 255, 255, 0.4),
      0px 0px 3px rgba(25, 0, 255, 0.6),
      0px 2px 5px rgba(25, 0, 255, 0.5),
      0px 5px 8px rgba(25, 0, 255, 0.4);
  }
  100% {
    text-shadow:
      0px 0px 1px rgba(255, 255, 255, 0.5),
      1px 0px 1px rgba(245, 9, 60, 0.6),
      2px 2px 4px rgba(240, 11, 11, 0.5) 4px 5px 6px rgba(242, 54, 220, 0.4);
  }
}
@media (min-width: 320px) {
  .container {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }
}

@media (min-width: 1200px) {
  .container {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }
}

@media (max-width: 992px) {
  .container {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }
}

span {
  display: flex;
  justify-self: end;
  margin-left: 60%;
  animation-duration: 3s;
  animation-delay: 1s;
  animation-name: slidein;
}

@keyframes slidein {
  from {
    margin-left: 100%;
    width: 0%;
  }

  to {
    margin-left: 60%;
    width: 100%;
  }
}
@media screen and (min-width: 480px) {
  span {
    display: flex;
    justify-self: end;
    margin-left: 80%;
    animation-duration: 3s;
    animation-delay: 1s;
    animation-name: slidein;
  }

  @keyframes slidein {
    from {
      margin-left: 100%;
      width: 0%;
    }

    to {
      margin-left: 80%;
      width: 100%;
    }
  }
}
@media screen and (max-width: 576px) and (min-width: 480px) {
  span {
    display: flex;
    justify-self: end;
    margin-left: 60%;
    animation-duration: 3s;
    animation-delay: 1s;
    animation-name: slidein;
  }

  @keyframes slidein {
    from {
      margin-left: 100%;
      width: 0%;
    }

    to {
      margin-left: 60%;
      width: 100%;
    }
  }
}
@media screen and (min-width: 1200px) {
  span {
    display: flex;
    justify-self: end;
    margin-left: 80%;
    animation-duration: 3s;
    animation-delay: 1s;
    animation-name: slidein;
  }

  @keyframes slidein {
    from {
      margin-left: 100%;
      width: 0%;
    }

    to {
      margin-left: 80%;
      width: 100%;
    }
  }
}
</style>
