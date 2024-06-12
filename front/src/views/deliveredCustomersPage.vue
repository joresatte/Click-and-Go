<!-- # @author: Jores Atte Mottoh
# @date: 14/12/2023
# @description: customersPage with methods, attributes and template
# @project: Click and Go
# @modified by:
# @modified date: -->

<template>
    <header>
        <AppLogo/>
    </header>
    <section class="customers">
        <section class="flex justify-content-between flex-wrap"  style="background-color: #707070; padding: 1em; border-radius: 0.5em;">
            <section class="flex justify-content-start">
                <span class="ml-1 p-input-icon-left ">
                    <i class="pi pi-search " style="color: blue;"/>
                    <InputText
                    type="text" v-model="filteredText"
                    placeholder="Buscar"
                    style="width: 8em; color: blue;"/>
                </span>
            </section>
            <section class="flex justify-content-end">
                <Button @click="toggle" >
                    <i class="pi pi-bars" style="color: white;" ></i>
                    </Button>
                <Menu ref="menu" id="config_menu" :model="items" popup />
            </section>
        </section>
            <div class="block bg-primary font-bold text-center p-4 border-round mb-3" style="margin-top: 10%;" v-if="showLoad">
            <div class="showLoad">{{ load }}</div>
        </div>
        <div class="list" v-show="showList">
            <div class="col-12" v-for="(item, index) in filteredData" :key="index">
                <div class="flex flex-column xl:flex-row xl:align-items-start p-4 gap-4" :class="{ 'border-top-1 surface-border': index !== 0 }"
                v-if="!filteredText=='' &&
                            item.cliente.toLowerCase().includes(filteredText.toLowerCase())||
                            item.address.toLowerCase().includes(filteredText.toLowerCase())||
                            item.phone.toLowerCase().includes(filteredText.toLowerCase())||
                            item.dni.toLowerCase().includes(filteredText.toLowerCase())||
                            item.status.toLowerCase().includes(filteredText.toLowerCase())? true: false">
                    <div class="flex flex-column sm:flex-row justify-content-between align-items-center xl:align-items-start flex-1 gap-4">
                        <div class="flex flex-column align-items-center sm:align-items-start gap-3 ">
                            <img class="w-4 sm:w-5rem xl:w-2rem shadow-2 block xl:block mx-auto border-round" :src="item.picture" alt="image client" />
                            <div class="text-2xl font-bold text-900">{{ item.cliente }}</div>
                            <span class="font-semibold">{{ item.address }}</span>
                            <span class="font-semibold">{{ item.dni}}</span>
                            <div class="flex align-items-center gap-3">
                                <span class="flex align-items-center gap-2">
                                    <i class="pi pi-tag"></i>
                                </span>
                            </div>
                        </div>
                        <div class="flex sm:flex-column align-items-center sm:align-items-end gap-3 sm:gap-2">
                            <span class="text-2xl font-semibold">{{ item.phone}}</span>
                            <Tag :value="item.status" :severity="getSeverity(item)"></Tag>
                            <Button icon="pi pi-eye"
                                label="ver"
                                :loading="loading"
                                class="btn-class-btn"
                                @click="onclicked(item.id, item.status)"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup>
import config from "@/config.js";
import { ref, onMounted, computed, toValue, onBeforeUpdate, watch} from "vue";
import {usePiniaStore} from '@/stores/store';
import AppLogo from "@/components/appLogo.vue";
const piniaStore= usePiniaStore();
const selectedData= ref();
const showList= ref(true);
const filteredText= ref('');
const selected = ref();
let currSeconds= ref(0);
let timer= ref(null);
const response= ref();
const fetching= ref(true);
const error= ref();
const menu = ref(null);
let loading= ref(false);
const load= ref('Loading...');
const showLoad= ref(true);
const showEmptyFilterMessage= ref(false);
const EmptyFilterMessage= ref('No hay datos disponibles');
const items = ref([
    {
        label: 'Refresh',
        icon: 'pi pi-refresh',
        command:()=>{
            window.location.reload();
        }
    },
    {
        label: 'Backward',
        icon: 'pi pi-arrow-left',
        command:()=>{
            piniaStore.router.push({
                path: '/optionPage',
                name: 'optionPage',
            })
        }
    },
    {
        label: 'Pending page',
        icon: 'pi pi-chevron-circle-right',
        command:()=>{
            piniaStore.router.push({
                path: '/pending',
                name: 'pending',
            })
        }
    },
    {
        label: 'Log out',
        icon: 'pi pi-sign-out',
        command:()=>{
            localStorage.clear();
            piniaStore.router.push({
                path: '/loginPage',
                name: 'loginPage',
            })
        }
    },
    {
        separator: true
    },
]);
onMounted(() => {
    loadData();
});
const loadData= async ()=>{
    try {
        const url= `${config.path}/delivered`;
        const options= {};
        await piniaStore.getData(toValue(url), options);
        response.value= await piniaStore.data.json();
        let isString= Object.prototype.toString.call(response.value) === "[object String]" ? true: false;
        console.log('isString', isString);
    } catch (errors) {
        error.value= errors;
    }finally{
        fetching.value= false;
        !error.value!=null && response.value!= null? showLoad.value= false: showLoad.value= true;
    }
        
};

const toggle = (event) => {
    menu.value.toggle(event);
};
const testJSON=(text)=> {
    if (typeof text !== "string") {
        JSON.stringify(text);
        JSON.parse(text);
        return true;
    }else{
        return false;
    }
};

window.onload= resetTimer();
window.onunload= resetTimer();
function resetTimer(){
    /* Clear the previous interval */ 
    clearInterval(timer.value); 

    /* Reset the seconds of the timer */ 
    currSeconds.value = 0; 

    /* Set a new interval */ 
    timer.value = 
        setInterval(startIdleTimer, 3600000); 
}

function startIdleTimer(){
    /* Increment the 
        timer seconds */ 
    currSeconds++;

    /* clear  identity data 
    after the page is loaded 
    according to the currSeconds value*/ 
    localStorage.clear('dataIdentity');
    //console.log(removeIdentidy)
}


const filtered= (val, obj)=>{
    if(!val==''){
        obj.reduce(function(acc, e) {
            if (e.status== val) {
                acc.push(e);
            }
            selectedData.value= acc;
            // return selectedData.value;
            }, []);
        return selectedData.value;
    }else{
        return response.value;
    }
}

function onSortChange(e){
    // localStorage.setItem('selectValue', e)
    selected.value=e;
}

let filteredData = computed(() => { 
    const val = selected.value;
    const obj= response.value;
    return filtered(val, obj);
    
})

watch(() => filteredData, () => {
    if (filteredData.length<4) {
        showGrid.value= false;
        console.log(showGrid.value);
    }
}, { immediate: true })

const getSeverity = (item) => {
    switch (item.status) {
        case 'Entregado':
            return 'success';

        case 'No entregado':
            return 'danger';

        default:
            return null;
    }
}

async function onclicked(e, s){
  if(piniaStore.router.path != `/client/${e}`){
      piniaStore.pathId= e;
      piniaStore.customerStatus= s;
      await piniaStore.router.push({
              path: `/client/:id`,
              name: 'customerDetails',
              params:{id: e}
              }).catch(err => {
                      // Ignore the vuex err regarding  navigating to the page they are already on.
                      if (
                      err.name !== 'NavigationDuplicated' &&
                      !err.message.includes('Avoided redundant navigation to current location')
                      ) {
                      // But print any other errors to the console
                      console.error(err);
                      }
                });
      
  }
  
};

</script>
<style scoped>
.p-dataview .p-dataview-header {
  background: #f9fafb;
  color: #374151;
  border: 1px solid #e5e7eb;
  border-width: 1px 0 1px 0;
  padding: 0rem 0rem;
  font-weight: 700;
  margin-bottom: 1em;
}
div:hover{
    background-color: #707070;
}
.customers{
    margin-top: 1.5em;
}
/* @media (hover: hover) {
    div:hover {
        background: rgb(243, 44, 127);
    }
} */
@media (min-width: 360px) {
    .btn-class-btn{
        width: 10em;
    }
}
</style>