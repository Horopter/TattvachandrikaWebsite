<template>
  <div class="container mt-5">
    <h2>Subscriber Types</h2>
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">Subscriber Types</li>
      </ol>
    </nav>

    <table class="table table-striped mt-4">
      <thead>
        <tr>
          <th>Name</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-if="addingNew">
          <td><input type="text" v-model="newSubscriberType.name" class="form-control" /></td>
          <td>
            <button class="btn btn-primary btn-sm" @click="saveNewSubscriberType">Save</button>
            <button class="btn btn-secondary btn-sm" @click="cancelNewSubscriberType">Cancel</button>
          </td>
        </tr>
        <tr v-for="type in subscriberTypes" :key="type._id">
          <template v-if="editMode === type._id">
            <td><input type="text" v-model="editSubscriberType.name" class="form-control" /></td>
            <td>
              <button class="btn btn-primary btn-sm" @click="updateSubscriberType(type._id)">Save</button>
              <button class="btn btn-secondary btn-sm" @click="cancelEdit">Cancel</button>
            </td>
          </template>
          <template v-else>
            <td>{{ type.name }}</td>
            <td>
              <button class="btn btn-warning btn-sm" @click="editSubscriberTypeFunc(type)">Edit</button>
              <button class="btn btn-danger btn-sm" @click="showDeleteModal(type._id)">Delete</button>
            </td>
          </template>
        </tr>
      </tbody>
    </table>
    <button class="btn btn-success mt-3" @click="startAddingNew">Add New Type</button>

    <confirmation-modal
      v-if="showConfirmationModal"
      :show="showConfirmationModal"
      title="Confirm Delete"
      message="Are you sure you want to delete this subscriber type?"
      @close="hideDeleteModal"
      @confirm="deleteSubscriberType"
    />
  </div>
</template>

<script>
import subscriberTypeService from '../services/subscriberTypeService';
import ConfirmationModal from './ConfirmationModal.vue';

export default {
  components: {
    ConfirmationModal
  },
  data() {
    return {
      subscriberTypes: [],
      addingNew: false,
      editMode: null,
      showConfirmationModal: false,
      typeToDelete: null,
      newSubscriberType: {
        name: ''
      },
      editSubscriberType: {
        name: ''
      }
    };
  },
  created() {
    this.loadSubscriberTypes();
  },
  methods: {
    loadSubscriberTypes() {
      subscriberTypeService.getSubscriberTypes().then(response => {
        this.subscriberTypes = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscriber types!", error);
      });
    },
    startAddingNew() {
      this.addingNew = true;
      this.resetNewSubscriberType();
    },
    cancelNewSubscriberType() {
      this.addingNew = false;
    },
    resetNewSubscriberType() {
      this.newSubscriberType = {
        name: ''
      };
    },
    saveNewSubscriberType() {
      subscriberTypeService.createSubscriberType(this.newSubscriberType).then(() => {
        this.loadSubscriberTypes();
        this.addingNew = false;
      }).catch(error => {
        console.error("There was an error saving the subscriber type!", error);
      });
    },
    editSubscriberTypeFunc(type) {
      this.editMode = type._id;
      this.editSubscriberType = { ...type };
    },
    cancelEdit() {
      this.editMode = null;
    },
    updateSubscriberType(id) {
      subscriberTypeService.updateSubscriberType(id, this.editSubscriberType).then(() => {
        this.loadSubscriberTypes();
        this.editMode = null;
      }).catch(error => {
        console.error("There was an error updating the subscriber type!", error);
      });
    },
    showDeleteModal(id) {
      this.typeToDelete = id;
      this.showConfirmationModal = true;
    },
    hideDeleteModal() {
      this.showConfirmationModal = false;
      this.typeToDelete = null;
    },
    deleteSubscriberType() {
      subscriberTypeService.deleteSubscriberType(this.typeToDelete).then(() => {
        this.loadSubscriberTypes();
        this.hideDeleteModal();
      }).catch(error => {
        console.error("There was an error deleting the subscriber type!", error);
      });
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>
