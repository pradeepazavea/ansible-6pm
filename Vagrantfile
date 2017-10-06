Vagrant.configure("2") do |config|
  config.vm.define "server1" do |server1|
    server1.vm.box = "bento/centos-7.2"
    server1.vm.network "private_network", ip: "192.168.50.10"
  end
  config.vm.define "server2" do |server2|
    server2.vm.box = "bento/centos-7.2"
    server2.vm.network "private_network", ip: "192.168.50.11"
  end
  config.vm.define "server3" do |server3|
    server3.vm.box = "ubuntu/trusty64"
    server3.vm.network "private_network", ip: "192.168.50.12"
  end
  config.vm.define "server4" do |server4|
    server4.vm.box = "ubuntu/trusty64"
    server4.vm.network "private_network", ip: "192.168.50.13"
  end
end

# Some comment
