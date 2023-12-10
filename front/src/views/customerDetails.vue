<template>
    <div>
        <AppLogo/>
    </div>
    <div class="flex align-items-stretch flex-wrap" style="min-height: 3em">
        <info class="flex align-items-center justify-content-center bg-primary px-3 py-1 font-bold border-round m-2" style="min-width: 200px; min-height: 50px" msg="Comprobante de la entrega"/>
    </div>
    <div class="block bg-primary font-bold text-center p-4 border-round mb-3" style="margin-top: 10%;" v-if="showLoad">
        <div class="showLoad">{{ load }}</div>
    </div>
    <div class="container">
        <div class="contain">
            <h1>Datos cliente</h1>
            <div class="customer">
                <h4>Cliente: {{ response.dict.cliente }}</h4>
                <h4>DNI: {{ response.dict.dni }}</h4>
                <h4>Direccion: {{ response.dict.address }}</h4>
                <h4>Telefono: {{ response.dict.phone }}</h4>
                <h4>Estado pedido: {{ response.dict.status }}</h4>
            </div>
        </div>
        <div class="contain">
            <h1 >Datos pedido</h1>
            <div class="customer">
                <h4>Fecha de entrega: {{ response.order_data.delivery_date }}</h4>
                <h4>Numero de pedido: {{ response.order_data.order_number}}</h4>
                <h4>Hora limite: {{ response.order_data.delivery_time }}</h4>
                <h4>Franja Horaria: {{ response.order_data.delivery_time_interval }}</h4>
            </div>
        </div>
        <div class="contain">
            <h1 >bultos pedido</h1>
            <div class="customer">
                <h4>{{ response.drawers.cold }}</h4>
                <h4>{{ response.drawers.frozen }}</h4>
                <h4>{{ response.drawers.dry }}</h4>
                <h4>{{ response.drawers.out_of_drawers }}</h4>
                <h4>{{ response.bags.cold }}</h4>
                <h4>{{ response.bags.frozen }}</h4>
                <h4>{{ response.orders_packages.substitutions}}</h4>
            </div>
        </div>
        <div class="contain">
            <div class="customer">
                <span class="p-float-label">
                    <Textarea v-model="response.delivery_note.note" rows="3" cols="35" style="margin-top: 5px;"/>
                    <label>Notas para reparto:</label>
                </span>
            </div>
        </div><br><br>
        <div class="contain">
            unidad de producto devueltos<br>
            <div class="return">
                <InputNumber v-model="response.returned_product.unity" inputId="horizontal-buttons" showButtons buttonLayout="horizontal" :step="1"
                    decrementButtonClass="p-button-danger" incrementButtonClass="p-button-success" incrementButtonIcon="pi pi-plus" decrementButtonIcon="pi pi-minus"
                    style=" width: 2em"/> <br><br>
                <span class="p-float-label">
                    <Textarea v-model="response.returned_product.return_reason" rows="2" cols="35" />
                    <label>Motivo de devoluciones:</label>
                </span>
            </div>
        </div>
    </div>
</template>
<script setup>
import { ref, onMounted, toValue, reactive} from "vue";
import AppLogo from "@/components/appLogo.vue";
import info from "@/components/info.vue";
import {usePiniaStore} from '@/stores/store'
import config from "@/config.js";
const piniaStore= usePiniaStore()
const response= reactive({
                            dict:{}, 
                            order_data:[], 
                            delivery_note:[], 
                            orders_packages: [], 
                            receptor_data:[], 
                            returned_product:[], 
                            drawers:[], bags:[]})
const load= ref('Loading...')
const fetching= ref(true)
const showLoad= ref(true)
const error= ref()
onMounted(() => {
    loadCustmer()
    console.log('customer details', loadCustmer())
});
const loadCustmer= async ()=>{

    try {
        const url= `${config.login_Path}/one_customer/${piniaStore.pathId}`
        console.log(url)
        const options= {}
        await piniaStore.getData(toValue(url), options)
        response.dict= await piniaStore.data
        console.log(response.dict)
        response.order_data= response.dict.order_data
        response.delivery_note= response.dict.delivery_note
        response.orders_packages= response.dict.orders_packages
        response.receptor_data= response.dict.receptor_data
        response.returned_product= response.dict.returned_product
        response.drawers= response.dict.orders_packages.drawers
        response.bags= response.dict.orders_packages.bags
        console.log(response.drawers)
        console.log(response.bags)

    } catch (errors) {
        error.value= errors
    }finally{
        fetching.value= false;
        !error.value!=null && response.dict!= null? showLoad.value= false: showLoad.value= true
    }
}

</script>
<style scoped>
    @media (min-width: 1024px) {
        .login {
            min-height: 100vh;
            display: flex;
            align-items: center;
        }
    }
    .container{
        display: block;
        border-radius: 5px;
        border: solid rgba(166, 171, 172, 0.185);
    }
    .customer{
        
        border-radius: 5px;
        border: solid rgba(166, 171, 172, 0.185);
    }
    @media (min-width: 1024px) {
        .container {
            min-height: 100vh;
            display: flex;
            align-items: center;
        }
    }
</style>