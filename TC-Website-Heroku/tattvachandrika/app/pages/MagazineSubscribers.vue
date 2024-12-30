<template>
  <div class="container mx-auto mt-8 px-4">
    <!-- Breadcrumb Navigation -->
    <nav aria-label="breadcrumb" class="mb-6">
      <ol class="flex space-x-2 text-gray-700">
        <li>
          <router-link to="/HomePage" class="text-blue-600 hover:text-blue-800 font-semibold">Home</router-link>
        </li>
        <li>
          <span>/</span>
        </li>
        <li class="text-gray-500 font-semibold" aria-current="page">Magazine Subscribers</li>
      </ol>
    </nav>

    <h2 class="text-3xl font-bold text-gray-800 mb-4">Magazine Subscribers</h2>
    <button class="bg-gradient-to-r from-blue-500 to-blue-600 text-white px-5 py-2 rounded-md shadow-md hover:bg-gradient-to-l transition duration-200 mb-4" @click="openEditSubscriberModal">Add Subscriber</button>

    <!-- Tabs for Active and Inactive Subscribers -->
    <ul class="flex border-b border-gray-300 mb-4">
      <li class="mr-4">
        <button class="py-2 px-6 text-lg font-medium text-gray-600 hover:text-blue-600 transition duration-200" :class="{ 'border-b-2 border-blue-600 text-blue-600': activeTab === 'active' }" @click="activeTab = 'active'">Active Subscribers</button>
      </li>
      <li>
        <button class="py-2 px-6 text-lg font-medium text-gray-600 hover:text-blue-600 transition duration-200" :class="{ 'border-b-2 border-blue-600 text-blue-600': activeTab === 'inactive' }" @click="activeTab = 'inactive'">Inactive Subscribers</button>
      </li>
    </ul>

    <div class="tab-content">
      <!-- Active Subscribers Tab -->
      <div v-show="activeTab === 'active'">
        <ul class="flex border-b border-gray-300 mb-4">
          <li class="mr-4">
            <button class="py-2 px-6 text-lg font-medium text-gray-600 hover:text-blue-600 transition duration-200" :class="{ 'border-b-2 border-blue-600 text-blue-600': activeSubTab === 'current' }" @click="activeSubTab = 'current'">Current Subscribers</button>
          </li>
          <li>
            <button class="py-2 px-6 text-lg font-medium text-gray-600 hover:text-blue-600 transition duration-200" :class="{ 'border-b-2 border-blue-600 text-blue-600': activeSubTab === 'renewal' }" @click="activeSubTab = 'renewal'">Waiting for Renewal</button>
          </li>
        </ul>
        
        <div class="tab-content">
          <!-- Current Subscribers Tab -->
          <div v-show="activeSubTab === 'current'">
            <table class="min-w-full bg-white divide-y divide-gray-300 shadow-md">
              <thead class="bg-gray-100">
                <tr>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Registration Number</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Name</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">City/Town</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">State</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Phone</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Email</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Actions</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="subscriber in currentSubscribers" :key="subscriber._id" class="hover:bg-gray-50 transition duration-200">
                  <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.registration_number }}</td>
                  <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.name }}</td>
                  <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.city_town }}</td>
                  <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.state }}</td>
                  <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.phone }}</td>
                  <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.email }}</td>
                  <td class="px-6 py-4 text-sm text-gray-800 flex space-x-2">
                    <nuxt-link :to="`/magazineSubscriberDetails?id=${subscriber._id}`">
                      <button class="bg-blue-600 text-white px-4 py-1 rounded-md text-xs shadow-sm hover:bg-blue-700 transition duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500">View</button>
                    </nuxt-link>
                    <button class="bg-gray-600 text-white px-4 py-1 rounded-md text-xs shadow-sm hover:bg-gray-700 transition duration-200 focus:outline-none focus:ring-2 focus:ring-gray-500" @click="openEditSubscriberModal(subscriber)">Edit</button>
                    <button class="bg-red-600 text-white px-4 py-1 rounded-md text-xs shadow-sm hover:bg-yellow-700 transition duration-200 focus:outline-none focus:ring-2 focus:ring-red-500" @click="confirmDeleteSubscriber(subscriber._id)">Delete</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          
          <!-- Waiting for Renewal Tab -->
          <div v-show="activeSubTab === 'renewal'">
            <table class="min-w-full bg-white divide-y divide-gray-300 shadow-md">
              <thead class="bg-gray-100">
                <tr>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Registration Number</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Name</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">City/Town</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">State</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Phone</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Email</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Actions</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="subscriber in waitingForRenewalSubscribers" :key="subscriber._id" class="hover:bg-gray-50 transition duration-200">
                  <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.registration_number }}</td>
                  <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.name }}</td>
                  <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.city_town }}</td>
                  <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.state }}</td>
                  <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.phone }}</td>
                  <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.email }}</td>
                  <td class="px-6 py-4 text-sm text-gray-800 flex space-x-2">
                    <nuxt-link :to="`/magazineSubscriberDetails?id=${subscriber._id}`">
                      <button class="bg-blue-600 text-white px-4 py-1 rounded-md text-xs shadow-sm hover:bg-blue-700 transition duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500">View</button>
                    </nuxt-link>
                    <button class="bg-gray-600 text-white px-4 py-1 rounded-md text-xs shadow-sm hover:bg-gray-700 transition duration-200 focus:outline-none focus:ring-2 focus:ring-gray-500" @click="openEditSubscriberModal(subscriber)">Edit</button>
                    <button class="bg-red-600 text-white px-4 py-1 rounded-md text-xs shadow-sm hover:bg-orange-700 transition duration-200 focus:outline-none focus:ring-2 focus:red-red-500" @click="confirmDeleteSubscriber(subscriber._id)">Delete</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      
      <!-- Inactive Subscribers Tab -->
      <div v-show="activeTab === 'inactive'">
        <table class="min-w-full bg-white divide-y divide-gray-300 shadow-md">
          <thead class="bg-gray-100">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Registration Number</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Name</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">City/Town</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">State</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Phone</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Email</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="subscriber in inactiveSubscribers" :key="subscriber._id" class="hover:bg-gray-50 transition duration-200">
              <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.registration_number }}</td>
              <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.name }}</td>
              <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.city_town }}</td>
              <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.state }}</td>
              <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.phone }}</td>
              <td class="px-6 py-4 text-sm text-gray-800">{{ subscriber.email }}</td>
              <td class="px-6 py-4 text-sm text-gray-800 flex space-x-2">
                <nuxt-link :to="`/magazineSubscriberDetails?id=${subscriber._id}`">
                  <button class="bg-blue-600 text-white px-4 py-1 rounded-md text-xs shadow-sm hover:bg-blue-700 transition duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500">View</button>
                </nuxt-link>
                <button class="bg-gray-600 text-white px-4 py-1 rounded-md text-xs shadow-sm hover:bg-gray-700 transition duration-200 focus:outline-none focus:ring-2 focus:ring-gray-500" @click="openEditSubscriberModal(subscriber)">Edit</button>
                <button class="bg-green-600 text-white px-4 py-1 rounded-md text-xs shadow-sm hover:bg-green-700 transition duration-200 focus:outline-none focus:ring-2 focus:ring-green-500" @click="activateSubscriber(subscriber._id)">Activate</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Add/Edit Subscriber Modal -->
    <add-edit-subscriber-modal 
      :show="showAddEditSubscriberModal" 
      :subscriber="selectedSubscriber" 
      :categories="categories" 
      :types="types" 
      @close="closeAddEditSubscriberModal" 
      @save="saveSubscriber">
    </add-edit-subscriber-modal>

    <!-- Confirmation Modal -->
    <confirmation-modal
      v-if="showConfirmationModal"
      :show="showConfirmationModal"
      title="Confirm Delete"
      message="Are you sure you want to delete this subscriber?"
      @close="hideDeleteModal"
      @confirm="deleteSubscriber"
    />

    <!-- Toast Notification -->
    <toast-notification ref="toast" />
  </div>
</template>

<script>
import AddEditSubscriberModal from './AddEditSubscriberModal.vue';
import ConfirmationModal from './ConfirmationModal.vue';
import magazineSubscriberService from '../services/magazineSubscriberService';

export default {
  components: {
    AddEditSubscriberModal,
    ConfirmationModal
  },
  data() {
    return {
      currentSubscribers: [],
      waitingForRenewalSubscribers: [],
      inactiveSubscribers: [],
      categories: [],
      types: [],
      showAddEditSubscriberModal: false,
      selectedSubscriber: null,
      showConfirmationModal: false,
      subscriberToDelete: null,
      activeTab: 'active',
      activeSubTab: 'current'
    };
  },
  created() {
    this.loadSubscribers();
    this.loadCategories();
    this.loadTypes();
  },
  methods: {
    loadSubscribers() {
      magazineSubscriberService.getMagazineSubscribers().then(response => {
        this.currentSubscribers = response.data.filter(subscriber => !subscriber.isDeleted && subscriber.hasActiveSubscriptions);
        this.waitingForRenewalSubscribers = response.data.filter(subscriber => !subscriber.isDeleted && !subscriber.hasActiveSubscriptions);
        this.inactiveSubscribers = response.data.filter(subscriber => subscriber.isDeleted);
      }).catch(error => {
        console.error("There was an error retrieving the subscribers!", error);
      });
    },
    loadCategories() {
      magazineSubscriberService.getCategories().then(response => {
        this.categories = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the categories!", error);
      });
    },
    loadTypes() {
      magazineSubscriberService.getTypes().then(response => {
        this.types = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the types!", error);
      });
    },
    openAddSubscriberModal() {
      this.selectedSubscriber = {
        registration_number: '',
        name: '',
        address: '',
        city_town: '',
        state: '',
        pincode: '',
        phone: '',
        email: '',
        category: '',
        stype: '',
        notes: ''
      };
      this.showAddEditSubscriberModal = true;
    },
    openEditSubscriberModal(subscriber) {
      this.selectedSubscriber = { ...subscriber };
      this.showAddEditSubscriberModal = true;
    },
    closeAddEditSubscriberModal() {
      this.showAddEditSubscriberModal = false;
    },
    saveSubscriber(subscriber) {
      if (subscriber._id) {
        magazineSubscriberService.updateMagazineSubscriber(subscriber._id, subscriber).then(() => {
          this.loadSubscribers();
          this.showAddEditSubscriberModal = false;
        }).catch(error => {
          console.error("There was an error updating the subscriber!", error);
        });
      } else {
        magazineSubscriberService.createMagazineSubscriber(subscriber).then(() => {
          this.loadSubscribers();
          this.showAddEditSubscriberModal = false;
        }).catch(error => {
          console.error("There was an error adding the subscriber!", error);
        });
      }
    },
    confirmDeleteSubscriber(subscriberId) {
      this.subscriberToDelete = subscriberId;
      this.showConfirmationModal = true;
    },
    hideDeleteModal() {
      this.showConfirmationModal = false;
    },
    deleteSubscriber() {
      if (this.subscriberToDelete) {
        magazineSubscriberService.softDeleteMagazineSubscriber(this.subscriberToDelete).then(() => {
          this.loadSubscribers();
          this.hideDeleteModal();
        }).catch(error => {
          console.error("There was an error deleting the subscriber!", error);
        });
      }
    },
    activateSubscriber(subscriberId) {
      magazineSubscriberService.activateMagazineSubscriber(subscriberId).then(() => {
        this.loadSubscribers();
      }).catch(error => {
        console.error("There was an error activating the subscriber!", error);
      });
    },
    viewSubscriber(subscriberId) {
      this.$router.push({ path: `/magazineSubscriberDetails?id=${subscriberId}` });
    }
  }
};
</script>

<style scoped>
.table {
  margin-top: 20px;
}
</style>
