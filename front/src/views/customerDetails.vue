<!-- # @author: Jores Atte Mottoh
# @date: 14/12/2023
# @description: customerDetails with methods, attributes and template
# @project: Click and Go
# @modified by:
# @modified date: -->

<template>
    <header>
        <AppLogo/>
    </header>
    <div class="flex align-items-stretch flex-wrap">
        <info class="flex align-items-center justify-content-center bg-primary px-3 py-1 font-bold border-round m-2" style="width: 50%;" msg="Comprobante de la entrega"/>
    </div> 
    <section class="block bg-primary font-bold text-center p-4 border-round" style="height: 4em;" v-if="showLoad">
       {{ load }}
    </section>
    <div class="container">
        <div class="contain">
            <h1>Datos cliente</h1>
            <div class="customer">
                <h4>Cliente:</h4> {{ response.dict.cliente }}
                <h4>DNI:</h4> {{ response.dict.dni }}
                <h4>Direccion:</h4> {{ response.dict.address }}
                <h4>Telefono:</h4> {{ response.dict.phone }}
                <h4>Estado pedido:</h4> {{ response.dict.status }}
            </div>
        </div>
        <div class="contain">
            <h1 >Datos pedido</h1>
            <div class="customer">
                <h4>Fecha de entrega:</h4> {{ response.order_data.delivery_date }}
                <h4>Numero de pedido:</h4> {{ response.order_data.order_number}}
                <h4>Hora limite:</h4> {{ response.order_data.delivery_time }}
                <h4>Franja Horaria:</h4> {{ response.order_data.delivery_time_interval }}
            </div>
        </div>
        <div class="contain">
            <h1 >Bultos pedido</h1>
            <div class="order_drawers">
                <section class="block_section">
                    <h2>Cajones</h2>
                    <div class="block_div flex flex-row flex-wrap justify-content-center align-items-center">
                        <div class="block">
                            <h4 class="flex flex-row flex-wrap justify-content-center align-items-center">Frio</h4><span class="span_block">{{ response.drawers.cold }}</span>
                        </div>
                        <div class="block">
                            <h4 class="flex flex-row flex-wrap justify-content-center align-items-center">Congelado</h4><span class="span_block">{{ response.drawers.frozen }}</span>
                        </div>
                        <div class="block">
                            <h4 class="flex flex-row flex-wrap justify-content-center align-items-center">Seco</h4><span class="span_block">{{ response.drawers.dry }}</span>
                        </div>
                        <div class="block">
                            <h4 class="flex flex-row flex-wrap justify-content-center align-items-center">Fuera de cajon</h4><span class="span_block">{{ response.drawers.out_of_drawers }}</span>
                        </div>
                    </div>
                </section>
                <section class="block_section">
                    <h2>Bolsas</h2>
                    <div class="block_div flex flex-row flex-wrap justify-content-center align-items-center">
                        <div class="block">
                            <h4 class="flex flex-row flex-wrap justify-content-center align-items-center">Frio</h4><span class="span_block">{{ response.bags.cold }}</span>
                        </div>
                        <div class="block">
                            <h4 class="flex flex-row flex-wrap justify-content-center align-items-center">Congelado</h4><span class="span_block">{{ response.bags.frozen }}</span>
                        </div>
                    </div>
                </section>
                <section class="block_section">
                    <h2>Sustituciones</h2>
                    <div class="block_div flex flex-row flex-wrap justify-content-center align-items-center">
                        <div class="block">
                            <h4 class="flex flex-row flex-wrap justify-content-center align-items-center">{{ response.orders_packages.substitutions}}</h4>
                        </div>
                    </div>
                </section>
            </div>
        </div>
        <div class="contain">
            <div class="textarea_1">
                <span class="p-float-label">
                    <Textarea id="myTextarea" v-model="response.delivery_note.note" rows="3" style="margin-top: 5px; width: 100%;"/>
                    <label>Notas para reparto:</label>
                </span>
            </div>
        </div><br>
        <div class="contain">
            <div class="return">
                <span class="p-float-label">
                    <Textarea id="textarea" v-model="response.returned_product.return_reason" rows="2" style="margin-top: 5px; width: 100%;"/>
                    <label>Devoluciones y motivo de devoluciones:</label>
                    <small id="textarea-help">apunta aqui los productos devueltos y el o los motivo(s) de la devolucion</small>
                </span> <br>
                unidad de producto devueltos<br>
                <div class="flex">
                    <InputNumber v-model="response.returned_product.unity" inputId="integeronly" style="width: 96%; height: 4em;"/>
                    <Button icon="pi pi-plus" aria-label="Submit" @click="response.returned_product.unity++" style="width: 5em; height: 4em;"/>
                </div>
            </div>
        </div>
    </div><br>
    <Message severity="error" :sticky="sticky" :life="6000" v-if="showErrorMessage">{{errorMessage}}</Message>
    <Message severity="success" :sticky="sticky" :life="1000" v-if="showSuccess">{{successMessage}}</Message>
    <div class="contain">
        <div class="receptor">
            <div class="card flex justify-content-center">
                <div class="flex flex-column gap-2">
                    <label for="dni">DNI del receptor</label>
                    <InputText id="dni" v-model="response.receptor_data.DNI" aria-describedby="dni-help" />
                    <!-- <small id="DNI-help">apunta aqui el DNI del recpetor del pedido.</small> -->
                </div>
            </div><br>
            <div class="card flex justify-content-center">
                <div class="flex flex-column gap-2">
                    <label for="username">Nombre del receptor</label>
                    <InputText id="username" v-model="response.receptor_data.name" aria-describedby="username-help" />
                    <!-- <small id="username-help">apunta aqui el nombre del recpetor del pedido.</small> -->
                </div>
            </div>
        </div>
    </div><br><br>
    <footer class="btn-footer" v-show="showBtn">
        <!-- <Button class="btn" 
        aria-label="btn" 
        @click="onclicked" severity="help" :style="styleObject">
            <i class="pi pi-send px-2" :loading="loading"></i>
            <span class="px-3">{{submit}}</span>
        </Button> -->
        <Button type="button" 
                id="btnOnclick"
                :label="submit" 
                severity="help" 
                icon="pi pi-send" 
                :loading="loading" 
                :style="styleObject"
                @click="onClicked" iconPos="left"/>
    </footer>
</template>
<script setup>
import { ref, onMounted, toValue, reactive, watch} from "vue";
import { useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'
import AppLogo from "@/components/appLogo.vue";
import info from "@/components/info.vue";
import {usePiniaStore} from '@/stores/store'
import config from "@/config.js";
const piniaStore= usePiniaStore()
const router = useRouter()
const loading= ref(false)
const response= reactive({
                            dict:{}, 
                            order_data:[], 
                            delivery_note:[], 
                            orders_packages: [], 
                            receptor_data:[], 
                            returned_product:[], 
                            drawers:[], bags:[], 
                            status:[]})
const load= ref('Loading...')
const fetching= ref(true)
const showLoad= ref(true)
const error= ref()
const showBtn= ref(false)
const submit= ref('Guardar')
let sticky = ref(true);
const showSuccess= ref(false)
const successMessage= ref('Successfully updated')
const errorMessage= ref('Es importante comprobar los siguientes datos: si hay devoluciones especificar la cantidad y tanto el Dni y nombre del receptor no pueden estar vacios')
const showErrorMessage= ref(false)
const styleObject = reactive({
  color: '#eeeeee',
  fontSize: '1em',
  backgroundColor:''
})
onMounted(() => {
    console.log('customer details page')
    loadCustmer()
    beforeLeave
    leavePath
    const ele=  document.getElementById("myTextarea").disabled= true;
    if(piniaStore.customerStatus== 'Entregado'){
      const el= document.getElementById("textarea").disabled= true;
      const dn= document.getElementById("dni").disabled=true;
      const us= document.getElementById("username").disabled= true;
      const btn= document.getElementById("btnOnclick").disabled= true;
      submit.value='Enviado'
      console.log(ele, el, dn, us)
    }
    
});
const beforeLeave= onBeforeRouteLeave(()=>{
    const answer= window.confirm('Dou you really want to leave, may check if you have some unsaved changes!')
    if(!answer)return false
    console.log('leave or not ')
})

const leavePath= onBeforeRouteUpdate (()=>{
    const redirection = piniaStore.getIdentity() && beforeLeave== true ?router.push({
        path: '/customersPage',
        name: 'customersPage',
    }): piniaStore.router.push({
        path: '/loginPage',
        name: 'loginPage',
    })
    console.log('To customerPage or loginPage')
})

const loadCustmer= async ()=>{

    try {
        const url= `${config.login_Path}/one_customer/${piniaStore.pathId}`
        const options= {}
        await piniaStore.getData(toValue(url), options)
        response.dict= await piniaStore.data.json()
        let isString= Object.prototype.toString.call(response.dict) === "[object String]" ? true: false
        console.log('isString', isString)
        response.order_data= response.dict.order_data
        response.delivery_note= response.dict.delivery_note
        response.orders_packages= response.dict.orders_packages
        response.receptor_data= response.dict.receptor_data
        response.returned_product= response.dict.returned_product
        response.drawers= response.dict.orders_packages.drawers
        response.bags= response.dict.orders_packages.bags
        response.status= response.dict.status
    } catch (errors) {
        error.value= errors
    }finally{
        fetching.value= false;
        !error.value!=null && response.dict!= null? showLoad.value= false: showLoad.value= true
    }
}

watch(() => [response.receptor_data.DNI, response.receptor_data.name], () => {
    if (response.receptor_data.DNI!='' && response.receptor_data.name!='') {
        console.log(true)
        showBtn.value= true
    }else{
        showBtn.value= false
    }
})

watch(() => submit.value, () => {
    if (submit.value== 'Enviado') {
        const btn= document.getElementById("btnOnclick").disabled= true;
        console.log('disable btn', btn)
        setTimeout(() => {
            showBtn.value= false
        }, 3000);
    }
}, { immediate: true })

const onClicked=async()=>{
    console.log('clicked')
    if(
       response.returned_product.return_reason!=''&& response.returned_product.unity!=''||
       response.returned_product.return_reason==''&& response.returned_product.unity=='' &&
       response.receptor_data.name!='' && response.receptor_data.DNI!=''
    ){
        styleObject.backgroundColor= '#59c88b'
        submit.value= 'Enviado'
        console.log(response.receptor_data.DNI ,response.receptor_data.name, 
        response.returned_product.return_reason, response.returned_product.unity)
        const url= `${config.login_Path}/customer_data/update/${piniaStore.pathId}`
        const options= {
            method: "PUT",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify({
                id: piniaStore.pathId,
                picture: response.dict.picture,
                cliente: response.dict.cliente,
                dni: response.dict.dni,
                address: response.dict.address,
                phone: response.dict.phone,
                status: 'Entregado',
                delivery_note:response.dict.delivery_note,
                order_data: response.dict.order_data,
                orders_packages: response.dict.orders_packages,
                receptor_data:response.receptor_data,
                returned_product:response.returned_product,
            }),
        }
        await piniaStore.getData(toValue(url), options)
        piniaStore.data.status==200? showSuccess.value=true:showErrorMessage.value=true
        loading.value = true;
        setTimeout(() => {
            loading.value = false;
        }, 1000);
        return submit.value
    }else{
        showErrorMessage.value=true
        styleObject.backgroundColor= 'red'
        submit.value= 'No enviado'
    }
}
</script>
<style scoped>
    @viewport {
    width: device-width;
    }
    .customer{
        width: 100%;
        border-radius: 5px;
        border: solid rgba(9, 43, 238, 0.185);
    }
    .textarea_1{
        width: 100%;
        margin-top: 2em;
        border-radius: 5px;
        border: solid rgba(9, 43, 238, 0.185);
    }
    .order_drawers{
        width: 100%;
        border-radius: 5px;
        border: solid rgba(9, 43, 238, 0.185);
    }
    .block{
        display: flex;
        align-items: center;
        width:8em;
        border: solid red;
    }
    h2{
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .span_block{
        display: flex;
        justify-content: center;
    }
    .btn-footer {
        padding: 1.5em;
        display: flex;
        border-top: 1px solid #eeeeee;
        flex-direction: column;
        justify-content: flex-end;
    }
    /* #btn:hover {
        border: 3px #f107a3;
    } */
    /* .btn{
        color: #eeeeee;
        font-size: 1em;
    } */
    /* @media (hover: hover) {
        btn:hover {
            background-color: rgb(243, 44, 127);
        }
} */
</style>