import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config';

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { aliases, mdi } from 'vuetify/iconsets/mdi'
import Button from 'primevue/button';
// import 'primevue/resources/themes/saga-blue/theme.css';
import "primevue/resources/themes/lara-light-indigo/theme.css";
import 'primevue/resources/primevue.min.css';                
import 'primeicons/primeicons.css';
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

const vuetify = createVuetify({
  components,
  directives,
})

export default createVuetify({
    icons: {
      defaultSet: 'mdi',
      aliases,
      sets: {
        mdi,
      },
    },
  })
  
const app= createApp(App);
app.use(vuetify)
app.use(router)
app.use(PrimeVue)
app.use(ToastService);
app.directive('tooltip', Tooltip);
app.component('Button', Button)
app.component('Toast', Toast)
app.component('InputText', InputText)
app.component('Toolbar', Toolbar)
app.component('Sidebar', Sidebar)
app.component('FileUpload', FileUpload)
app.component('InputNumber', InputNumber)
app.component('ColorPicker', ColorPicker)
app.component('MultiSelect', MultiSelect)
app.component('Textarea', Textarea)
app.component('Dropdown', Dropdown)
app.component('Menu', Menu)
app.component('Rating', Rating)
app.component('InlineMessage', InlineMessage)

app.mount('#app')

