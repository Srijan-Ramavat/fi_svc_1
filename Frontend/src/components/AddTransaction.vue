<template>
  <div  class="app-container">
    <h1>Add Transaction</h1>
    <a-form ref="form" :model="formState" @submit="onSubmit">
      <a-form-item label="Category">
        <a-select
          v-model:value="formState.category"
          placeholder="please select category"
          required
        >
          <a-select-option value="Groceries">Groceries</a-select-option>
          <a-select-option value="Travel">Travel</a-select-option>
          <a-select-option value="Books">Book</a-select-option>
        </a-select>
      </a-form-item>
      <a-form-item label="Date">
        <a-date-picker
          v-model:value="formState.date1"
          type="date"
          placeholder="Pick a date"
          style="width: 100%"
          required
        />
      </a-form-item>
      <a-form-item label="Amount">
        <a-input-number v-model:value="formState.amount" style="width: 100%" ></a-input-number>
      </a-form-item>
      <a-form-item label="Description">
        <a-textarea v-model:value="formState.desc"></a-textarea>
      </a-form-item>
      <a-form-item>
        <a-button type="primary" :disabled="!isValid" @click="onSubmit" style="width: 100%">Save</a-button>
      </a-form-item>
      <a-form-item>
        <a-button @click="resetForm" style="width: 100%">Clear</a-button>
      </a-form-item>
    </a-form>
  </div>
</template>
<script>
import axios from 'axios';

import {
  Button,
  Select,
  SelectOption,
  InputNumber,
  Form,
  FormItem,
  DatePicker,
  Textarea
} from "ant-design-vue";

export default {
  name: "AddTransaction",
  components: {
    "a-button": Button,
    "a-select": Select,
    "a-select-option": SelectOption,
    "a-form": Form,
    "a-input-number": InputNumber,
    "a-form-item": FormItem,
    "a-textarea": Textarea,
    "a-date-picker": DatePicker,
  },
  data() {
    return {
      formState: {
        amount: undefined,
        category: undefined,
        date1: undefined,
        desc: "",
      },
      isValid : false,
    };
  },
  methods: {
    async onSubmit() {
      let transaction = {};
      let date = this.formState.date1.format('YYYY-MM-DD');
      transaction.date = date;
      transaction.amount = this.formState.amount;
      transaction.description = this.formState.desc;
      transaction.category = this.formState.category;
      console.log("submit!", transaction);
      let response = await axios.post("http://127.0.0.1:8000/api/transactions/", transaction);
      console.log(response)
      if(response.status === 201) {
        this.resetForm();
      }
    },
    resetForm() {
      this.formState = {
        amount: undefined,
        category: undefined,
        date1: undefined,
        desc: "",
      };
    },
    checkValid() {
      if ((this.formState.amount !== undefined || this.formState.amount !== null)
        && this.formState.category !== undefined 
        && this.formState.date1 !== undefined) {
        this.isValid = true;
      } else {
        this.isValid = false;
      }
    },
  },
  watch: {
    'formState.amount': {
      handler: function(newValue, oldValue) {
        if (isNaN(newValue)) {
          this.formState.amount = oldValue;
        }
        console.log(this.formState.amount);
        this.checkValid();
      },
      deep: true
    },
    'formState.category': {
      handler: function() {
        this.checkValid();
      },
      deep: true
    },'formState.date1': {
      handler: function() {
        this.checkValid();
      },
      deep: true
    },
  }
};
</script>
<style scoped>
.app-container{
  max-width: 400px;
  margin: auto;
  display: flex;
  flex-direction: column; 
}
</style>
