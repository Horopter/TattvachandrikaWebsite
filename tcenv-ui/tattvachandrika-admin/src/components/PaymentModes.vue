<template>
  <div class="container mt-5">
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">Payment Modes</li>
      </ol>
    </nav>
    <h2>Payment Modes</h2>
    <button class="btn btn-primary mb-3" @click="addMode">Add Payment Mode</button>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>Name</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="mode in paymentModes" :key="mode._id">
          <td>
            <input v-if="editModeId === mode._id" type="text" v-model="mode.name" />
            <span v-else>{{ mode.name }}</span>
          </td>
          <td>
            <button class="btn btn-success btn-sm" v-if="editModeId === mode._id" @click="saveMode(mode)">Save</button>
            <button class="btn btn-warning btn-sm" v-else @click="editMode(mode._id)">Edit</button>
            <button class="btn btn-danger btn-sm" @click="confirmDeleteMode(mode._id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>

    <confirmation-modal
      v-if="showConfirmationModal"
      :show="showConfirmationModal"
      title="Confirm Delete"
      message="Are you sure you want to delete this payment mode?"
      @close="hideDeleteModal"
      @confirm="deleteMode"
    />
  </div>
</template>

<script>
import paymentModeService from '../services/paymentModeService';
import confirmationModal from './ConfirmationModal.vue';

export default {
  components: {
    confirmationModal
  },
  data() {
    return {
      paymentModes: [],
      editModeId: null,
      showConfirmationModal: false,
      modeToDelete: null
    };
  },
  created() {
    this.loadPaymentModes();
  },
  methods: {
    loadPaymentModes() {
      paymentModeService.getPaymentModes().then(response => {
        this.paymentModes = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the payment modes!", error);
      });
    },
    addMode() {
      const newMode = {
        name: ''
      };
      this.paymentModes.unshift(newMode);
      this.editModeId = newMode._id;
    },
    editMode(modeId) {
      this.editModeId = modeId;
    },
    saveMode(mode) {
      if (mode._id) {
        paymentModeService.updatePaymentMode(mode._id, mode).then(() => {
          this.loadPaymentModes();
          this.editModeId = null;
        }).catch(error => {
          console.error("There was an error updating the payment mode!", error);
        });
      } else {
        paymentModeService.createPaymentMode(mode).then(() => {
          this.loadPaymentModes();
          this.editModeId = null;
        }).catch(error => {
          console.error("There was an error creating the payment mode!", error);
        });
      }
    },
    confirmDeleteMode(modeId) {
      this.modeToDelete = modeId;
      this.showConfirmationModal = true;
    },
    hideDeleteModal() {
      this.showConfirmationModal = false;
    },
    deleteMode() {
      if (this.modeToDelete) {
        paymentModeService.deletePaymentMode(this.modeToDelete).then(() => {
          this.loadPaymentModes();
          this.hideDeleteModal();
        }).catch(error => {
          console.error("There was an error deleting the payment mode!", error);
        });
      }
    }
  }
};
</script>

<style scoped>
.table {
  margin-top: 20px;
}
</style>
