<template>
  <div class=" page-label"><h1 >{{label}}</h1></div>
  <loginEmployee 
    :login="loginUser"
    @onChanged="onChanged"
    @onclicked=" onclicked"
  />
  <Toast />
</template>
<script setup>
import { ref, reactive} from 'vue';
import config from "@/config.js";
import loginEmployee from './components/loginEmployee.vue';
// import getLoginPost from './views/apiSrevives/getLoginPost';
// import {useFetch} from './views/apiSrevives/loginPost'
import { useToast } from "primevue/usetoast";
import { useRouter, useRoute } from 'vue-router'
const toast = useToast();
const router = useRouter()
const route = useRoute()
const label= ref('Eroski')
const loginUser = reactive({
  identification: '',
  password: ''
})

const onChanged=(e)=>{
  loginUser.value= e
}

async function onclicked(){
  console.log('Send button clicked')
  const settings = reactive({
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        identification: loginUser['identification'],
        password: loginUser['password']
    }),
  })
  if(loginUser['identification'] && loginUser['password'] != ''){
        const response = await fetch(`${config.login_Path}/get_login/Authenticated`, settings)
        const requestStatusCode = response.status
        console.log('request Status Code ', requestStatusCode)
        if(requestStatusCode==200){
          // toast.add({ severity: 'success', summary: 'success Message', detail: 'Successfully', group: 'bl', life: 1000 });
          router.push({
                        path: '/',
                        name: 'home'
                      })
        }
        else{
          toast.add({ severity: 'error', summary: 'Error Message', detail: 'Failed to login', life: 4000 });
      }
  }else{
    toast.add({ severity: 'error', summary: 'Error Message', detail: 'All fields are required', life: 3000 });
  }
}
</script>

<style scoped>
.page-label{
  text-align: center;
  color: red;
}
</style>