<template>
  <div class="card">
      <DataView :value="customers" :layout="layout" :sortOrder="sortOrder" :sortField="sortField">
          <template #header>
              <div class="overflow-hidden">
                  <div class="flex">
                      <Dropdown v-model="sortKey" 
                          class="flex justify-content-start font-bold border-round"
                          :options="sortOptions" optionLabel="label" placeholder="Filtrar" @change="onSortChange($event)" />
                          <span class="ml-1 p-input-icon-left ">
                              <i class="pi pi-search " style="color: blue;"/>
                              <InputText 
                              type="text" v-model="filterByText" 
                              placeholder="Buscar" 
                              style="width: 8em; color: blue;"/>
                          </span>
                      <DataViewLayoutOptions v-model="layout"
                          class="flex-1 flex justify-content-end font-bold border-round"/>
                  </div>
              </div>
          </template>
              <template #list="" v-for="index in customers" :key="index.id">
                  <div class="col-12" >
                      <div class="flex flex-column xl:flex-row xl:align-items-start p-4 gap-4" >
                          <div class="flex flex-column sm:flex-row justify-content-between align-items-center xl:align-items-start flex-1 gap-4">
                              <div class="flex flex-column align-items-center sm:align-items-start gap-3">
                                  <img class="w-4 sm:w-5rem xl:w-2rem shadow-2 block xl:block mx-auto border-round" src="@/assets/img/_copy.jpg" alt="image client" />
                                  <div class="text-2xl font-bold text-900">{{ index.cliente }}</div>
                                  <span class="font-semibold">{{ index.address }}</span>
                                  <span class="font-semibold">{{ index.dni }}</span>
                                  <!-- <Rating :modelValue="slotProps.data.rating" readonly :cancel="false"></Rating> -->
                                  <div class="flex align-items-center gap-3">
                                      <span class="flex align-items-center gap-2">
                                          <i class="pi pi-tag"></i>
                                      </span>
                                  </div>
                              </div>
                              <div class="flex sm:flex-column align-items-center sm:align-items-end gap-3 sm:gap-2">
                                  <span class="text-2xl font-semibold">{{ index.phone }}</span>
                                  <Tag severity="success" value="Success"></Tag>
                                  <Button icon="pi pi-eye"
                                          label="ver"
                                          :loading="loading"
                                          @click="onclicked(index.id)"/>
                              </div>
                          </div>
                      </div>
                  </div>
              </template>
              <template #grid="" v-for="index in customers" :key="index.id">
                  <div class="col-12 sm:col-6 lg:col-12 xl:col-4 p-2" >
                      <div class="p-4 border-1 surface-border surface-card border-round" >
                          <div class="flex flex-wrap align-items-center justify-content-between gap-2">
                              <!-- <Tag :value="slotProps.data.inventoryStatus" :severity="getSeverity(slotProps.data)"></Tag> -->
                          </div>
                          <div class="flex flex-column align-items-center gap-3 py-5">
                              <img class="w-4 sm:w-5rem xl:w-2rem shadow-2 block xl:block mx-auto border-round" src="@/assets/img/_copy.jpg" alt="image client" />
                              <div class="text-2xl font-bold">{{ index.cliente }}</div>
                              <span class="font-semibold">{{ index.address }}</span>
                              <div class="flex align-items-center gap-2">
                                  <span class="text-2xl font-semibold">{{ index.phone}}</span>
                              </div>
                              <div class="flex align-items-center justify-content-between">
                                  <span class="font-semibold">{{ index.dni }} </span>
                                  <i class="pi pi-tag"></i>
                              </div>
                              <div class="flex sm:flex-column align-items-center sm:align-items-start gap-3 sm:gap-2">
                                  <Tag severity="success" value="Success"></Tag>
                              </div>
                              <div class="flex sm:flex-column align-items-center sm:align-items-end gap-3 sm:gap-2">
                                  <Button icon="pi pi-eye"
                                          label="ver"
                                          :loading="loading"
                                          @click="onclicked(index.id)"/>
                              </div>
                          </div>
                          
                      </div>
                  </div>
              </template>
      </DataView>
  </div>
  <RouterView />
</template>


<script setup>
import config from "@/config.js";
import { ref, onMounted, computed} from "vue";
import { useRouter } from 'vue-router'

onMounted(() => {
loadData()
});

const filterByText= ref()
const sortKey = ref();
const sortOrder = ref();
const sortField = ref();
const sortOptions = ref([
  {label: 'Entregdo', value: 'Success'},
  {label: 'No entregdo', value: '!Success'},
]);
const customers = ref();
const layout = ref('grid');
const error= ref(null)
let loading= ref(false)
const router = useRouter()

const loadData= async ()=>{
const response = await fetch(`${config.login_Path}/all_customers`)
          .catch((err) => (error.value = err))
  customers.value= await response.json()
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

computed(()=>{
  filterCustomers
  console.Console(filterCustomers)
})

const isValidFilter= async ()=>{
  console.log(await customers.value)
  for (const item of loadData){
      if (
          item.cliente.toLowerCase().includes(filterByText.value.toLowerCase())||
          item.dni.toLowerCase().includes(filterByText.value.toLowerCase())||
          item.address.toLowerCase().includes(filterByText.value.toLowerCase())||
          item.phone.toLowerCase().includes(filterByText.value.toLowerCase())
      ){
          return true
      }
  }
}
const filterCustomers= async ()=>{
  const data= await customers.value
  console.log(data)
  if (isValidFilter){
      return data.filter((item)=>{
          item.cliente.toLowerCase().includes(filterByText.value.toLowerCase())||
          item.dni.toLowerCase().includes(filterByText.value.toLowerCase())||
          item.address.toLowerCase().includes(filterByText.value.toLowerCase())||
          item.phone.toLowerCase().includes(filterByText.value.toLowerCase())
  })
  }else{
      return customers.value
  }
}

const onSortChange = (event) => {
  const value = event.value.value;
  const sortValue = event.value;

  if (value.indexOf('!') === 0) {
      sortOrder.value = -1;
      sortField.value = value.substring(1, value.length);
      sortKey.value = sortValue;
  }
  else {
      sortOrder.value = 1;
      sortField.value = value;
      sortKey.value = sortValue;
  }
};

const getSeverity = (product) => {
switch (product.inventoryStatus) {
    case 'INSTOCK':
        return 'success';

    case 'LOWSTOCK':
        return 'warning';

    case 'OUTOFSTOCK':
        return 'danger';

    default:
        return null;
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