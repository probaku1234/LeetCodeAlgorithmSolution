https://leetcode.com/explore/learn/card/system-design/689/system-design-basics/4409/

class DCLoadBalancer {
    private static final class Application {
        private final int id, load;

        public Application(int id, int load) {
            this.id = id;
            this.load = load;
        }

        public int getId() {
            return id;
        }
    }

    private static final class Machine implements Comparable<Machine> {
        private final int id;
        private int capacity;
        private final List<Application> applications = new ArrayList<>();

        public Machine(int id, int capacity) {
            this.id = id;
            this.capacity = capacity;
        }

        @Override
        public int compareTo(Machine o) {
            int result = Integer.compare(o.capacity, capacity);
            if (result == 0) result = Integer.compare(id, o.id);
            return result;
        }

        public void addApplication(Application application) {
            capacity -= application.load;
            applications.add(application);
        }

        public void stopApplication(int appId) {
            for (int i = 0; i < applications.size(); i++) {
                if (applications.get(i).id == appId) {
                    Application application = applications.remove(i);
                    capacity += application.load;
                    break;
                }
            }
        }
    }

    private final PriorityQueue<Machine> machinesPriorityQueue = new PriorityQueue<>();
    private final Map<Integer, Integer> mapAppIdToMachine = new HashMap<>();
    private final Map<Integer, Machine> mapIdToMachine = new HashMap<>();

    public DCLoadBalancer() {

    }

    public void addMachine(int machineId, int capacity) {
        Machine machine = new Machine(machineId, capacity);
        machinesPriorityQueue.add(machine);
        mapIdToMachine.put(machineId, machine);
    }

    public void removeMachine(int machineId) {
        Machine machine = mapIdToMachine.get(machineId);
        machinesPriorityQueue.remove(machine);
        mapIdToMachine.remove(machineId);
        machine.applications.forEach(application -> mapAppIdToMachine.remove(application.getId()));
        machine.applications.forEach(application -> addApplication(application.getId(), application.load));
    }

    public int addApplication(int appId, int loadUse) {
        Application application = new Application(appId, loadUse);
        Machine machine = findMachineByCapacity(loadUse);
        if (machine == null) return -1;
        machine.addApplication(application);
        machinesPriorityQueue.add(machine);
        mapAppIdToMachine.put(appId, machine.id);
        return machine.id;
    }

    private Machine findMachineByCapacity(int loadUse) {
        Machine machine = machinesPriorityQueue.peek();
        if (machine != null && machine.capacity >= loadUse) {
            return machinesPriorityQueue.poll();
        }
        return null;
    }

    public void stopApplication(int appId) {
        int machineId = mapAppIdToMachine.get(appId);
        Machine machine = mapIdToMachine.get(machineId);
        machine.stopApplication(appId);
        reorderMachineInPriorityQueue(machine);
    }

    private void reorderMachineInPriorityQueue(Machine machine) {
        machinesPriorityQueue.remove(machine);
        machinesPriorityQueue.add(machine);
    }

    public List<Integer> getApplications(int machineId) {
        Machine machine = mapIdToMachine.get(machineId);
        if (machine == null) return null;
        return machine.applications.stream().map(Application::getId).limit(10).collect(Collectors.toList());
    }
}