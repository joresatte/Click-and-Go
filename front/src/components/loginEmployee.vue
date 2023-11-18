<template>
  <div class="modal-backdrop">
    <div class="modal">
        <header class="modal-header">
            <slot name="header">
            all camps are required!
            </slot>
        </header>
        <section class="modal-body">
        <slot name="body">
            <span class="p-input-icon-right">
                <i class="pi pi-user" />
                <InputText v-model="login.identification" 
                          type="text" 
                          placeholder="enter your identifiction" 
                          @input='onChanged'
                          v-tooltip.bottom="'Enter your identifiction'"/>
            </span><br><br>
            <span class="p-input-icon-left">
                <Password v-model="login.password"
                            size="normal" 
                            placeholder="enter your password"
                            v-tooltip.bottom="'Enter your password'" 
                            @input= 'onChanged'
                            class="input-test"
                            toggleMask
                            />
            </span>
        </slot><br><br>
        </section>
        <footer class="modal-footer">
          <Button type="button" 
                  label="Log in" 
                  severity="help" 
                  icon="pi pi-send" 
                  :loading="loading" 
                  @click="onclicked" iconPos="right"/>
        </footer>
    </div>
</div> 
</template>

<script setup>
import { ref, reactive} from 'vue';

const props= defineProps({
    login: {
        type: Object,
        required: true
  }
})
const emit= defineEmits(['input', 'onChanged', 'onclicked'])
const user= reactive(props.login)
let loading= ref(false)
const onChanged=()=>{
    // const employee = JSON.parse(JSON.stringify(user))
    emit('onChanged', {...user})
    
}
function onclicked(){
    emit('onclicked')
    loading.value = true;
    setTimeout(() => {
        loading.value = false;
    }, 1000);
}
</script>

<style scoped>
.modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(233, 18, 18, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal {
    background: #fffffff8;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
}

.modal-header,
.modal-footer {
    padding: 1.5em;
    display: flex;
    border-top: 1px solid #eeeeee;
    flex-direction: column;
    justify-content: flex-end;
}

.modal-header {
    position: relative;
    border-bottom: 1px solid #eeeeee;
    color: #4AAE9B;
    justify-content: space-between;
}

.modal-body {
    position: relative;
    padding: 2em 2em;
}
</style>