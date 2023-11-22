<template>
  <div class=" page-label"><h1 >{{label}}</h1></div>
  <div v-if="showModal">
    <loginEmployee 
    :login="loginUser"
    @onChanged="onChanged"
    @onclicked=" onclicked"
    />
  </div>
  <RouterView />
  <Toast />
</template>

<script setup>
import {RouterView } from 'vue-router'
import { ref, reactive, onMounted} from 'vue';
import config from "@/config.js";
import loginEmployee from './components/loginEmployee.vue';
import { useToast } from "primevue/usetoast";
import { useRouter } from 'vue-router'

const toast = useToast();
const router = useRouter()
const label= ref('Eroski')
const error= ref(null)
const alert= ref(false)
const data= ref(null)
const showModal= ref(true)
const loginUser = reactive({
  identification: '',
  password: ''
})
onMounted(() => {
  if(window.localStorage){
     if(localStorage.getItem('dataIdentity')!== undefined && localStorage.getItem('dataIdentity') ){
      showModal.value= false
      router.push({
          path: '/home page',
          name: 'home page',
        })
     }else{
       return
     }
  }
});

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
      const response= await fetch(`${config.login_Path}/get_login/Authenticated`, settings)
                              .catch((err) => (error.value = err))
      const requestStatusCode = response.ok
      console.log('request Status Code ', requestStatusCode)
      if(requestStatusCode== true){
        data.value= await response.json()
        console.log(data.value)
        localStorage.setItem('dataIdentity', JSON.stringify(data.value))
        showModal.value= false
        router.push({
          path: '/home page',
          name: 'home page',
        })
      }
      if(!requestStatusCode== true){
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
