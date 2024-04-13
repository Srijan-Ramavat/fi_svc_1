<template>
    <div class="graph-container">
      <GChart type="PieChart" :data="chartData" :options="chartOptions" />
    </div>
  </template>
  
  <script>
  import { GChart } from "vue-google-charts";
  
  export default {
    name: "PieChart",
    props: ["chartData"],
    components: { GChart },
    data() {
      return {
        chartOptions: {
          is3D: true,
          backgroundColor: "transparent",
          chartArea: {
            height: "100%",
            width: "100%"
          }
        }
      };
    }
  };
  </script>
  
  <style scoped>
  .graph-container {
    display: flex;
    justify-content: center;
    width: 100%;
  }
  </style>