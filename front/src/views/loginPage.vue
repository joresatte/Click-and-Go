<!-- # @author: Jores Atte Mottoh
# @date: 14/12/2023
# @description: loginPage with methods, attributes and template
# @project: Click and Go
# @modified by:
# @modified date: -->

<template>
  <app-header /><br />
  <div class="login">
    <loginEmployee :login="loginUser" @onChanged="onChanged" @onclicked="onclicked" />
  </div>
  <Toast />
</template>
<script setup>
import loginEmployee from '@/components/loginEmployee.vue'
import { ref, reactive, onMounted } from 'vue'
import config from '@/config.js'
import appHeader from '@/components/appLogo.vue'
import { useToast } from 'primevue/usetoast'
import { usePiniaStore } from '@/stores/store'
const piniaStore = usePiniaStore()
const toast = useToast()
const error = ref(null)
const data = ref(null)
const loginUser = reactive({
  identification: '',
  password: ''
})
onMounted(() => {
  console.log('login page')
})

const onChanged = (e) => {
  loginUser.value = e
}
async function onclicked() {
  console.log('Send button clicked')
  const settings = reactive({
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      identification: loginUser['identification'],
      password: loginUser['password']
    })
  })
  if (loginUser['identification'] && loginUser['password'] != '') {
    const response = await fetch(`${config.path}/auth`, settings).catch(
      (err) => (error.value = err)
    )
    const requestStatusCode = response.ok
    console.log('request Status Code ', requestStatusCode)
    if (requestStatusCode == true) {
      data.value = await response.json()
      console.log(data.value)
      localStorage.setItem('dataIdentity', JSON.stringify(data.value))
      piniaStore.router.push({
        path: '/optionPage',
        name: 'optionPage'
      })
    }
    if (!requestStatusCode == true) {
      toast.add({
        severity: 'error',
        summary: 'Error Message',
        detail: 'Failed to login',
        life: 4000
      })
    }
  } else {
    toast.add({
      severity: 'error',
      summary: 'Error Message',
      detail: 'All fields are required',
      life: 3000
    })
  }
}
</script>

<style>
@media (min-width: 1024px) {
  .login {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
