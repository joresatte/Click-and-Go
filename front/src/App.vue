<template>
  <div class=" page-label"><h1 >{{label}}</h1></div>
  <div v-if="showHomePage"><home-view/></div>
  <div v-if="showModal">
    <loginEmployee 
    :login="loginUser"
    @onChanged="onChanged"
    @onclicked=" onclicked"
  />
  </div>
  <Toast />
</template>
<script setup>
import { ref, reactive, onMounted} from 'vue';
import config from "@/config.js";
import loginEmployee from './components/loginEmployee.vue';
import { useToast } from "primevue/usetoast";
import HomeView from './views/HomeView.vue';

onMounted(() => {
  if(window.localStorage){
     if(localStorage.getItem('dataIdentity')!== undefined && localStorage.getItem('dataIdentity') ){
       return showHomePage.value= true, showModal.value= false
     }else{
       return showHomePage.value= false, showModal.value= true
     }
  }
});
const toast = useToast();
const label= ref('Eroski')
const showModal= ref(true)
const showHomePage= ref(false)
const error= ref(null)
const data= ref(null)
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
      const response= await fetch(`${config.login_Path}/get_login/Authenticated`, settings)
                              .catch((err) => (error.value = err))
      const requestStatusCode = response.status
      console.log('request Status Code ', requestStatusCode)
      if(requestStatusCode== 200){
        data.value= await response.json()
        console.log(data.value)
        localStorage.setItem('dataIdentity', JSON.stringify(data.value))
        showModal.value= false
        showHomePage.value= true
      }
      if(error.value){
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