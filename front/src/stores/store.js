import { ref} from 'vue'
import { defineStore } from 'pinia'
import { useRouter, useRoute } from 'vue-router'
export const usePiniaStore = defineStore('Store', () => {

  const showTemplate= ref(false)
  const router = useRouter()
  const route = useRoute()
  const getIdentity=()=>{
    if(window.localStorage){
      if(localStorage.getItem('dataIdentity')!== undefined && localStorage.getItem('dataIdentity') ){
        // piniaStore.showModal= false
        return true
      }else{
        return false
      }
    }
  }
  
  return {  
    router,
    showTemplate,
    route,
    getIdentity,
   }
})
