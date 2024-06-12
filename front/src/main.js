import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config';

import "primevue/resources/themes/lara-light-indigo/theme.css";
import 'primevue/resources/primevue.min.css';                
import 'primeicons/primeicons.css';
import 'primeflex/primeflex.css'
import Button from 'primevue/button';
import DataView from 'primevue/dataview';
import InputText from 'primevue/inputtext';
import Toast from 'primevue/toast';
import ToastService from 'primevue/toastservice';
import Toolbar from 'primevue/toolbar';
import Sidebar from 'primevue/sidebar';
import Tooltip from 'primevue/tooltip';
import FileUpload from 'primevue/fileupload';
import InputNumber from 'primevue/inputnumber';
import ColorPicker from 'primevue/colorpicker';
import MultiSelect from 'primevue/multiselect';
import Textarea from 'primevue/textarea';
import Dropdown from 'primevue/dropdown';
import Menu from 'primevue/menu';
import Rating from 'primevue/rating';
import InlineMessage from 'primevue/inlinemessage';
import Password from 'primevue/password';
import Tag from 'primevue/tag';
import DataViewLayoutOptions from 'primevue/dataviewlayoutoptions'   // optional
import Message from 'primevue/message';
import Panel from 'primevue/panel';
import Avatar from 'primevue/avatar';
import AvatarGroup from 'primevue/avatargroup';   //Optional for grouping

const app= createApp(App);
app.use(createPinia())
app.use(ToastService);
app.use(PrimeVue)
app.use(router)
app.directive('tooltip', Tooltip);
app.component('DataView', DataView)
app.component('Tag', Tag)
app.component('Button', Button)
app.component('Toast', Toast)
app.component('InputText', InputText)
app.component('Password', Password)
app.component('Toolbar', Toolbar)
app.component('Sidebar', Sidebar)
app.component('FileUpload', FileUpload)
app.component('InputNumber', InputNumber)
app.component('ColorPicker', ColorPicker)
app.component('DataViewLayoutOptions', DataViewLayoutOptions)
app.component('MultiSelect', MultiSelect)
app.component('Textarea', Textarea)
app.component('Dropdown', Dropdown)
app.component('Menu', Menu)
app.component('Rating', Rating)
app.component('InlineMessage', InlineMessage)
app.component('Message', Message)
app.component('Panel', Panel)
app.component('Avatar', Avatar)
app.component('AvatarGroup ', AvatarGroup )

app.mount('#app')