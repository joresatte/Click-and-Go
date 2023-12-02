<template>
    <div class="flex justify-content-start font-bold border-round">
        <div class="flex justify-content-start font-bold border-round" style="margin-bottom: 1em;">
            <Dropdown v-model="selected"
                :options="options" optionLabel="text" placeholder="Filtrar" @change="onSortChange(selected.value)" />
        </div>
    </div>
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
    <div class="flex justify-content-between flex-wrap"  style="background-color: gray; padding: 1em; border-radius: 0.5em;">
        <div class="flex justify-content-start">
            <span class="ml-1 p-input-icon-left ">
                <i class="pi pi-search " style="color: blue;"/>
                <InputText 
                type="text" v-model="filteredText" 
                placeholder="Buscar" 
                style="width: 8em; color: blue;"/>
            </span>
        </div>
        <div class="flex justify-content-end">
            <Button @click="activeShowList" ><i class="pi pi-bars" style="color: white;" ></i></Button>
            <Button @click="activeShowGrid" ><i class="pi pi-th-large" style="color: white;" ></i></Button>
        </div>
    </div>
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
                    <div class="flex flex-column align-items-center sm:align-items-start gap-3">
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
                            @click="onclicked(item.id)"/>
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
                                @click="onclicked(item.id)"/>
                    </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import config from "@/config.js";
import { ref, onMounted, computed, toValue, onBeforeUpdate} from "vue";
import { useRouter } from 'vue-router'

const selectedData= ref()
const showGrid= ref(true)
const showList= ref(false)
const filteredText= ref('')
const selected = ref();
const options = ref([
  {text: 'Entregado', value: 'Entregado'},
  {text: 'No entregado', value: 'No entregado'},
]);
const response= ref()
const fetching= ref(true)
const error= ref()

let loading= ref(false)
const router = useRouter()
const load= ref('Loading...')
const showLoad= ref(true)

onMounted(() => {
    loadData()
})
const loadData= async ()=>{
    try {
        const url= `${config.login_Path}/all_customers`
        const options= {}
        let res= await fetch(toValue(url), options);
        let resJson = await res.json();
        let isString= Object.prototype.toString.call(resJson) === "[object String]" ? true: false
        console.log('isString', isString)   
        response.value= resJson
        console.log(Object.keys(response.value))
    } catch (errors) {
        error.value= errors
    }finally{
        fetching.value= false;
        !error.value!=null && response.value!= null? showLoad.value= false: showLoad.value= true
    }
        
}

const activeShowGrid=()=>{
    console.log('showGrid')
    showList.value= false
    showGrid.value= true
}
const activeShowList=()=>{
    console.log('showList')
    showGrid.value= false
    showList.value= true
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

const filtered= (val, obj)=>{
    if(!val==''){
        obj.reduce(function(acc, e) {
            console.log(e)
            if (e.status== val) {
                acc.push(e);
            }
            console.log(acc)
            selectedData.value= acc
            return selectedData.value
            }, []);
        return selectedData.value
    }else{
        return response.value
    }
}

function onSortChange(e){
    console.log(e)
    // localStorage.setItem('selectValue', e)
    selected.value=e
}

onBeforeUpdate(()=>{
    console.log(filteredData)
})

let filteredData = computed(() => { 
    const val = selected.value
    console.log(val)
    const obj= response.value
    return filtered(val, obj)
    
})


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

async function onclicked(e){
  console.log(e)
  localStorage.setItem('pathId', JSON.stringify(e))
  if(router.path != `/client/${e}`){
      await router.push({
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


</style>