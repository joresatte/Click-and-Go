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
        <section class="flex justify-content-start font-bold border-round">
            <section class="flex justify-content-start font-bold border-round" style="margin-bottom: 1em;">
                <Dropdown v-model="selected"
                    :options="options" optionLabel="text" placeholder="Filtrar" @change="onSortChange(selected.value)" />
            </section>
        </section>
        <!-- <div>
            <div style="margin-bottom: 0.5em;">
                <select v-model="selected" style="height: 3em; padding: 0.5em; border-radius: 0.5em; ">
                    <option value="">filter</option>
                    <option v-for="option in options" :value="option.value">
                        {{ option.text }}
                    </option>
                </select>
            </div>
        </div> -->
        <section class="flex justify-content-between flex-wrap"  style="background-color: gray; padding: 1em; border-radius: 0.5em;">
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
                <Button @click="activeShowList" ><i class="pi pi-bars" style="color: white;" ></i></Button>
                <Button @click="activeShowGrid" id="btnGrid" v-if="showGridBtn"><i class="pi pi-th-large" style="color: white;" ></i></Button>
            </section>
        </section>
            <div class="block bg-primary font-bold text-center p-4 border-round mb-3" style="margin-top: 10%;" v-if="showLoad">
            <div class="showLoad">{{ load }}</div>
        </div>
        <Message severity="error" :sticky="sticky" :life="6000" v-if="showMessage">{{redirection}}</Message>
        <Message severity="error" :sticky="sticky" :life="6000" v-if="showEmptyFilterMessage">{{EmptyFilterMessage}}</Message>
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
                                @click="onclicked(item.id, item.status)"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="grid" v-show="showGrid" >
            <div class="grid grid-nogutter" >
                <div class="col-12 sm:col-6 lg:col-12 xl:col-4 p-2" v-for="(item, index) in filteredData" :key="index">
                    <div class="p-4 border-1 surface-border surface-card border-round"
                    v-if="!filteredText=='' &&
                            item.cliente.toLowerCase().includes(filteredText.toLowerCase())||
                            item.address.toLowerCase().includes(filteredText.toLowerCase())||
                            item.phone.toLowerCase().includes(filteredText.toLowerCase())||
                            item.dni.toLowerCase().includes(filteredText.toLowerCase())||
                            item.status.toLowerCase().includes(filteredText.toLowerCase())? true: false"
                            >
                        <div class="flex flex-wrap align-items-center justify-content-between gap-2">
                        </div>
                        <div class="flex flex-column align-items-center gap-3 py-5">
                        <img class="w-4 sm:w-5rem xl:w-2rem shadow-2 block xl:block mx-auto border-round" :src="item.picture" alt="image client"
                        />
                        <div class="text-2xl font-bold"
                        >{{ item.cliente}}</div>
                        <span class="font-semibold"
                        >{{ item.address }}</span>
                        <div class="flex align-items-center gap-2"
                        >
                            <span class="text-2xl font-semibold">{{ item.phone}}</span>
                        </div>
                        <div class="flex align-items-center justify-content-between"
                        >
                            <span class="font-semibold">{{ item.dni }} </span>
                            <span
                            >
                                <i class="pi pi-tag"
                                ></i>
                            </span>
                        </div>
                        <div class="flex sm:flex-column align-items-center sm:align-items-start gap-3 sm:gap-2"
                        >
                            <Tag :value="item.status" :severity="getSeverity(item)"></Tag>
                        </div>
                        <div class="flex sm:flex-column align-items-center sm:align-items-end gap-3 sm:gap-2"
                        >
                            <Button icon="pi pi-eye"
                                    label="ver"
                                    :loading="loading"
                                    @click="onclicked(item.id, item.status)"/>
                        </div>
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
import {usePiniaStore} from '@/stores/store'
import AppLogo from "@/components/appLogo.vue";
const piniaStore= usePiniaStore()
const selectedData= ref()
const showGrid= ref(true)
const showGridBtn= ref(true)
const showList= ref(false)
const filteredText= ref('')
const selected = ref();
let currSeconds= ref(0)
let timer= ref(null)
const showMessage= ref(false)
const redirection= ref('Darle click a las tres barras para ver los datos filtrados')
const options = ref([
  {text: 'Entregado', value: 'Entregado'},
  {text: 'No entregado', value: 'No entregado'},
]);
const response= ref()
const fetching= ref(true)
const error= ref()
let sticky = ref(true);
let loading= ref(false)
const load= ref('Loading...')
const showLoad= ref(true)
const showEmptyFilterMessage= ref(false)
const EmptyFilterMessage= ref('No hay datos disponibles')
onMounted(() => {
    loadData()
    const redirection = piniaStore.getIdentity()== true ? piniaStore.router.push({
        path: '/customersPage',
        name: 'customersPage',
    }): piniaStore.router.push({
        path: '/loginPage',
        name: 'loginPage',
    })
    console.log('customers Page')
})
const loadData= async ()=>{
    try {
        const url= `${config.login_Path}/all_customers`
        const options= {}
        await piniaStore.getData(toValue(url), options)
        response.value= await piniaStore.data.json()
        let isString= Object.prototype.toString.call(response.value) === "[object String]" ? true: false
        console.log('isString', isString)
    } catch (errors) {
        error.value= errors
    }finally{
        fetching.value= false;
        !error.value!=null && response.value!= null? showLoad.value= false: showLoad.value= true
    }
        
}

const activeShowGrid=()=>{
    showList.value= false
    showGrid.value= true
}
const activeShowList=()=>{
    showGrid.value= false
    showList.value= true
    showMessage.value= false
}

const testJSON=(text)=> {
    if (typeof text !== "string") {
        JSON.stringify(text);
        JSON.parse(text)
        return true;
    }else{
        return false
    }
}

// function filterBy(val, obj) {
//     var objList = []
//   if(!val==''){
//     var result = Object.keys(obj).reduce(function(r, e) {
//     console.log(e)
//     if (e.indexOf(val) != -1) {
//         console.log(e.indexOf(val))
//         objList.push(obj[e]);
//     } else {
//       Object.values(obj[e]).filter(function(k) {
//         console.log(k)
//         if (k.status== val) {
//             // object[k] = obj[e][k];
//             // r[e] = object;
//             console.log(obj[e])
//             r.push(obj[e])
//         }
//       })
//     }
//     return r;
//     }, {})
//     return objList;
//   }
// }
window.onload= resetTimer()
window.onunload= resetTimer()
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
    localStorage.clear('dataIdentity')
    //console.log(removeIdentidy)
}


const filtered= (val, obj)=>{
    if(!val==''){
        obj.reduce(function(acc, e) {
            if (e.status== val) {
                acc.push(e);
            }
            selectedData.value= acc
            if(selectedData.value==0){
                showEmptyFilterMessage.value=true
                showGrid.value= true
            }
            else if (selectedData.value.length>0 && selectedData.value.length<4) {
                showGrid.value= false
                const btn= document.getElementById("btnGrid").disabled= true;
                if (showList.value== true){
                    showMessage.value= false
                }else showMessage.value= true
            }else{
                showMessage.value= false
                showEmptyFilterMessage.value= false
                showGrid.value= true
                // const btn= document.getElementById("btnGrid").disabled= false;
                // console.log('disable btn', btn)
            }
            return selectedData.value
            }, []);
        return selectedData.value
    }else{
        return response.value
    }
}

function onSortChange(e){
    // localStorage.setItem('selectValue', e)
    selected.value=e
}

onBeforeUpdate(()=>{
    console.log('before update')
})

let filteredData = computed(() => { 
    const val = selected.value
    const obj= response.value
    return filtered(val, obj)
    
})

watch(() => filteredData, () => {
    if (filteredData.length<4) {
        showGrid.value= false
        console.log(showGrid.value)
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
      piniaStore.pathId= e
      piniaStore.customerStatus= s
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
                })
      
  }
  
}

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
    background-color: rgb(243, 44, 127);
}
@media (hover: hover) {
    div:hover {
        background: rgb(243, 44, 127);
    }
}
</style>