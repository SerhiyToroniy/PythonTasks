using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace SwiftTransferAPI.Models
{
    public class JsonDescription
    {
        public uint total { get; set; }
        public uint limit { get; set; }
        public uint offset { get; set; }
        public uint returned { get; set; }
        public List<SwiftTransfer> data { get; set; }

        public JsonDescription()
        {
            total = 0;
            limit = 0;
            offset = 0;
            returned = 0;
            data = new List<SwiftTransfer>();
        }

        public JsonDescription(uint total, uint limit, uint offset, uint returned, List<SwiftTransfer> data)
        {
            this.total = total;
            this.limit = limit;
            this.offset = offset;
            this.returned = returned;
            this.data = data;
        }
    }
}
