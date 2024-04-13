<template>
  <div class="app-container">
    <h1>Analyze Trends</h1>

    <pie-chart v-if="!loading" :chartData="pieChartData" />
    <bar-chart v-if="!loading" :chartData="barChartData" />
  </div>
</template>

<script>
import axios from "axios";
import PieChart from '../components/PieChart.vue';
import BarChart from '../components/BarChart.vue';

export default {
  name: "SpendTrend",
  components: {
    PieChart,
    BarChart
  },
  data() {
    return {
      pieChartData: [
        ["Category", "Spend"],
      ],
      barChartData: [
        ["Date", "Groceries", "Travel", "Books"],
      ],
      transactionsPerCategory: undefined,
      dateWiseSpends: undefined,
      loading: true,
    };
  },
  methods: {
    async getSpends() {
      let response = await axios.get("http://127.0.0.1:8000/api/insights/");
      this.transactionsPerCategory = response.data.transactions_per_category;
      this.dateWiseSpends = response.data.date_wise_spends_per_category;
      this.transactionsPerCategory.map(obj => {
        this.pieChartData.push([obj.category , obj.total]);
      });

      let datewiseMap = new Map();

      this.dateWiseSpends.map(obj => {

        let groceries = 0;
        if (obj.category === "Groceries") {
          groceries = obj.total;
        }
        let travel = 0;
        if (obj.category === "Travel") {
          travel = obj.total;
        }
        let book = 0;
        if (obj.category === "Books") {
          book = obj.total;
        }
        if(!datewiseMap.has(obj.date)) { 
          datewiseMap.set(obj.date,[groceries,travel,book]);
        } else {
          let value = datewiseMap.get(obj.date);
          if(groceries !== 0) value[0] = groceries;
          if(travel !== 0) value[1] = travel;
          if(book !== 0) value[2] = book;
          datewiseMap.set(obj.date,value);
        }
      });
      datewiseMap.forEach((value,key) => {
        this.barChartData.push([key].concat(value));
      });
      this.loading = false;
      console.log(this.barChartData);

    },
  },
  mounted() {
    this.getSpends();
  },
};
</script>

<style scoped>
.app-container {
  max-width: 600px;
  margin: auto;
  display: flex;
  flex-direction: column;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
