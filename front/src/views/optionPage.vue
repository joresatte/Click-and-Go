
<template>
    <header>
        <AppLogo/>
    </header>
    <div class="div-class-wrapper">
        <div class="card1">
            <Toast />
            <Panel toggleable>
                <template #header class="template-class-header">
                    <div class="flex align-items-center gap-2">
                        <Avatar image="./src/assets/img/_copy.jpg" size="large" shape="circle" @click="clicked"/>
                        <span class="font-bold" @click="clicked">{{pending}}</span>
                    </div>
                </template>
                <template #footer>
                    <div class="flex flex-wrap align-items-center justify-content-between gap-3">
                        <div class="flex align-items-center gap-2">
                            <Button icon="pi pi-user" rounded text></Button>
                            <Button icon="pi pi-bookmark" severity="secondary" rounded text></Button>
                        </div>
                        <span class="p-text-secondary" v-if="showUpdated" >Last Updated: {{ lastUpdateDateTime }}</span>
                    </div>
                </template>
                <template #icons>
                    <button class="p-panel-header-icon p-link mr-2" @click="toggle">
                        <span class="pi pi-cog"></span>
                    </button>
                    <Menu ref="menu" id="config_menu" :model="items" popup />
                </template>
                <p class="m-0">
                    <i>total:</i> {{ pendingDataLength }}
                </p>
            </Panel>
        </div>
        <div class="card2">
            <Toast />
            <Panel toggleable>
                <template #header class="template-class-header">
                    <div class="flex align-items-center gap-2">
                        <Avatar image="./src/assets/img/_copy.jpg" size="large" shape="circle" @click="onclicked"/>
                        <span class="font-bold" @click="onclicked">{{delivered}}</span>
                    </div>
                </template>
                <template #footer>
                    <div class="flex flex-wrap align-items-center justify-content-between gap-3">
                        <div class="flex align-items-center gap-2">
                            <Button icon="pi pi-user" rounded text></Button>
                            <Button icon="pi pi-bookmark" severity="secondary" rounded text></Button>
                        </div>
                        <span class="p-text-secondary" v-if="showUpdated" >Last Updated: {{ lastUpdateDateTime }}</span>
                    </div>
                </template>
                <template #icons>
                    <button class="p-panel-header-icon p-link mr-2" @click="toggle">
                        <span class="pi pi-cog"></span>
                    </button>
                    <Menu ref="menu" id="config_menu" :model="items" popup />
                </template>
                <p class="m-0">
                    <i>total:</i> {{ deliveredDataLength }}
                </p>
            </Panel>
        </div>
    </div>
</template>

<script setup>
import AppLogo from "@/components/appLogo.vue";
import config from "@/config.js";
import { ref, onMounted, toValue } from 'vue';
import { useToast } from "primevue/usetoast";
import { useRouter } from 'vue-router';
// import Menu from 'primevue/menu';
import {usePiniaStore} from '@/stores/store'
const delivered= ref('Delivered customers');
const pending= ref('Pending customers');
const deliveredDataLength= ref(null);
const pendingDataLength= ref(null);
const pendingData= ref();
const deliveredData= ref();
const menu = ref(null);
const toast = useToast();
const router = useRouter();
const piniaStore= usePiniaStore();
let date= new Date();
let currentDateTime= ref(date.toLocaleString());
let lastUpdateDateTime= ref();
let count= ref(0);
const showUpdated= ref(false);
const error= ref();
const items = ref([
    {
        label: 'Refresh',
        icon: 'pi pi-refresh',
        command:()=>{
            lastUpdateDateTime.value= date.toLocaleDateString();
            showUpdated.value= true;
            if (count.value < count.value + 1) {
                lastUpdateDateTime.value= currentDateTime.value;
                count.value+=1;
            }
            setInterval(() => {
                let date = new Date();
                currentDateTime.value = date.toLocaleString();
            }, 1000);
        }
    },
    {
        separator: true
    },
]);

const toggle = (event) => {
    menu.value.toggle(event);
};

const clicked=()=>{
    console.log('on pending');
    piniaStore.router.push({
          path: '/pending',
          name: 'pending',
        })
};
const onclicked=()=>{
    console.log('on delivered');
    piniaStore.router.push({
          path: '/delivered',
          name: 'delivered',
        })
};

onMounted(() => {
    loadPendingData();
    loadDeliveredData();
    // const redirection = piniaStore.getIdentity()== true ? piniaStore.router.push({
    //     path: '/optionPage',
    //     name: 'optionPage',
    // }): piniaStore.router.push({
    //     path: '/loginPage',
    //     name: 'loginPage',
    // })
});

const loadPendingData= async ()=>{
    try {
        const url= `${config.path}/pending`;
        const options= {};
        await piniaStore.getData(toValue(url), options);
        pendingData.value= await piniaStore.data.json();
        pendingDataLength.value= pendingData.value.length;
        let isString= Object.prototype.toString.call(response.value) === "[object String]" ? true: false;
        console.log('isString', isString);
    } catch (errors) {
        error.value= errors;
    }
        
};
const loadDeliveredData= async ()=>{
    try {
        const url= `${config.path}/delivered`;
        const options= {};
        await piniaStore.getData(toValue(url), options);
        deliveredData.value= await piniaStore.data.json();
        deliveredDataLength.value= deliveredData.value.length;
        let isString= Object.prototype.toString.call(response.value) === "[object String]" ? true: false;
        console.log('isString', isString);
    } catch (errors) {
        error.value= errors;
    }
        
};

</script>
<style scoped>
    body{
        display: flex;
        justify-content: center;
        width: 100%;
        margin-top:10em;
        gap: 1em;
    }
    /* .div-class-wrapper{
        display: flex;
        justify-content: center;
        flex-direction: column-reverse;
        width: 100%;
        margin-top:10em;
        gap: 1em;
    } */
    .card1{
        margin-top: 5em;
    }
    .card2{
        margin-top: 1em;
    }
</style>