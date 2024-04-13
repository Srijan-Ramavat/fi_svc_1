<template>
  <SpendTrends v-if="showSpendTrends"/>
  <AddTransaction v-else />
  <a-button @click="toggleComponent">
    <template v-if="showSpendTrends">Add Transaction</template>
    <template v-else>Analyze</template>
  </a-button>
</template>

<script>
import SpendTrends from './components/SpendTrends.vue';
import AddTransaction from './components/AddTransaction.vue';
import { Button } from 'ant-design-vue';

export default {
  name: 'App',
  components: {
    SpendTrends,
    AddTransaction,
    'a-button': Button
  },
  data() {
    return {
      showSpendTrends: true
    }
  },
  methods: {
    toggleComponent() {
      this.showSpendTrends =!this.showSpendTrends;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
