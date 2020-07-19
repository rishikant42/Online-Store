<template>
  <div>
    <el-table
      ref="multipleTable"
      :data="tableData"
      style="width: 100%"
      @selection-change="handleSelectionChange"
    >
      <el-table-column type="selection" width="55"> </el-table-column>
      <el-table-column property="name" label="Product" width="120">
      </el-table-column>
    </el-table>
    <div style="margin-top: 20px">
      <el-button @click="toggleSelection([tableData[1], tableData[2]])"
        >Toggle selection status of second and third rows</el-button
      >
      <el-button @click="toggleSelection()">Clear selection</el-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: [
        {
          uid: "c3bc8cd3-a8ef-4423-af4b-71ba4d0012e7",
          name: "s1c2",
          category: {
            uid: "d68e6f22-ab1b-416e-8700-405b6d565e81",
            name: "c2"
          }
        }
      ],
      multipleSelection: []
    };
  },
  methods: {
    toggleSelection(rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },
    getProducts() {
      console.log("hello world");
      var api = "http://127.0.0.1:8000/api/store/products/";
      this.axios.get(api).then(response => {
        console.log(response.data);
      });
    }
  },
  mounted() {
    this.getProducts();
  }
};
</script>
